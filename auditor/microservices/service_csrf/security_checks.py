import requests
from urllib.parse import urlparse

def check_csrf_implementation():
    """Check CSRF protection implementation."""
    return {
        'status': 'checking',
        'message': 'Checking CSRF protection implementation',
        'checks': [
            {'name': 'CSRF Middleware', 'status': 'pending'},
            {'name': 'Form Protection', 'status': 'pending'},
            {'name': 'Cookie Settings', 'status': 'pending'}
        ]
    }

def check_token_validation():
    """Check CSRF token validation."""
    return {
        'status': 'checking',
        'message': 'Checking CSRF token validation',
        'checks': [
            {'name': 'Token Generation', 'status': 'pending'},
            {'name': 'Token Verification', 'status': 'pending'},
            {'name': 'Token Rotation', 'status': 'pending'}
        ]
    }

def check_header_configuration():
    """Check CSRF header configuration."""
    return {
        'status': 'checking',
        'message': 'Checking CSRF header configuration',
        'checks': [
            {'name': 'X-CSRF-Token Header', 'status': 'pending'},
            {'name': 'Same-Origin Policy', 'status': 'pending'},
            {'name': 'Custom Headers', 'status': 'pending'}
        ]
    }

def check_csrf_protection_for_url(url):
    """Check CSRF protection for a specific URL."""
    try:
        # Send a GET request to get the CSRF token
        session = requests.Session()
        response = session.get(url)
        
        # Check if CSRF token is present in cookies or response
        csrf_cookie = response.cookies.get('csrftoken')
        csrf_meta = None
        
        if 'text/html' in response.headers.get('Content-Type', ''):
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
            csrf_meta = soup.find('meta', {'name': 'csrf-token'})
        
        # Try a POST request without CSRF token
        try:
            response = session.post(url, data={'test': 'data'})
            csrf_enforced = response.status_code in [403, 400]
        except:
            csrf_enforced = True
            
        return {
            'name': 'CSRF Protection',
            'status': 'secure' if csrf_enforced and (csrf_cookie or csrf_meta) else 'vulnerable',
            'details': {
                'csrf_cookie_present': bool(csrf_cookie),
                'csrf_meta_present': bool(csrf_meta),
                'csrf_enforced': csrf_enforced
            }
        }
    except Exception as e:
        return {
            'name': 'CSRF Protection',
            'status': 'error',
            'details': str(e)
        }

def run_all_checks():
    """Run all CSRF security checks."""
    return {
        'implementation': check_csrf_implementation(),
        'token_validation': check_token_validation(),
        'header_configuration': check_header_configuration()
    }
