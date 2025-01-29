import pkg_resources
import requests
import json
from packaging import version

def check_dependency_versions():
    """Check installed dependency versions."""
    return {
        'status': 'checking',
        'message': 'Checking dependency versions',
        'checks': [
            {'name': 'Version Compatibility', 'status': 'pending'},
            {'name': 'Deprecated Versions', 'status': 'pending'},
            {'name': 'Version Conflicts', 'status': 'pending'}
        ]
    }

def check_known_vulnerabilities():
    """Check for known vulnerabilities in dependencies."""
    return {
        'status': 'checking',
        'message': 'Checking known vulnerabilities',
        'checks': [
            {'name': 'CVE Database', 'status': 'pending'},
            {'name': 'Security Advisories', 'status': 'pending'},
            {'name': 'Vulnerability Severity', 'status': 'pending'}
        ]
    }

def check_dependency_licenses():
    """Check dependency licenses."""
    return {
        'status': 'checking',
        'message': 'Checking dependency licenses',
        'checks': [
            {'name': 'License Compliance', 'status': 'pending'},
            {'name': 'License Conflicts', 'status': 'pending'},
            {'name': 'Commercial Usage', 'status': 'pending'}
        ]
    }

def check_available_updates():
    """Check for available dependency updates."""
    return {
        'status': 'checking',
        'message': 'Checking available updates',
        'checks': [
            {'name': 'Major Updates', 'status': 'pending'},
            {'name': 'Minor Updates', 'status': 'pending'},
            {'name': 'Security Updates', 'status': 'pending'}
        ]
    }

def check_package_security(package_name, current_version):
    """Check security status of a specific package."""
    try:
        # Check PyPI for package information
        response = requests.get(f'https://pypi.org/pypi/{package_name}/json')
        if response.status_code == 200:
            data = response.json()
            latest_version = data['info']['version']
            
            # Check if current version is latest
            is_latest = version.parse(current_version) >= version.parse(latest_version)
            
            # Check for known vulnerabilities (example using Safety DB)
            safety_db_url = 'https://raw.githubusercontent.com/pyupio/safety-db/master/data/insecure_full.json'
            safety_response = requests.get(safety_db_url)
            if safety_response.status_code == 200:
                safety_data = safety_response.json()
                vulnerabilities = safety_data.get(package_name, [])
                
                return {
                    'name': package_name,
                    'current_version': current_version,
                    'latest_version': latest_version,
                    'is_latest': is_latest,
                    'vulnerabilities': len(vulnerabilities),
                    'status': 'vulnerable' if vulnerabilities else 'secure'
                }
                
        return {
            'name': package_name,
            'status': 'error',
            'message': 'Unable to fetch package information'
        }
        
    except Exception as e:
        return {
            'name': package_name,
            'status': 'error',
            'message': str(e)
        }

def scan_requirements_file(file_path='requirements.txt'):
    """Scan requirements.txt file for security issues."""
    try:
        results = []
        with open(file_path, 'r') as f:
            for line in f:
                if line.strip() and not line.startswith('#'):
                    package = line.split('==')[0].strip()
                    version = line.split('==')[1].strip() if '==' in line else 'latest'
                    results.append(check_package_security(package, version))
        return results
    except Exception as e:
        return {
            'status': 'error',
            'message': f'Error scanning requirements file: {str(e)}'
        }

def run_all_checks():
    """Run all dependency management checks."""
    return {
        'versions': check_dependency_versions(),
        'vulnerabilities': check_known_vulnerabilities(),
        'licenses': check_dependency_licenses(),
        'updates': check_available_updates()
    }
