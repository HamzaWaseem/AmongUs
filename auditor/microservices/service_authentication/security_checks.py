import re
import requests
from urllib.parse import urlparse

def check_https_configuration(url):
    """Check HTTPS configuration of the target URL."""
    parsed_url = urlparse(url)
    return {
        'name': 'HTTPS Configuration',
        'status': 'secure' if parsed_url.scheme == 'https' else 'vulnerable',
        'details': 'Connection is encrypted' if parsed_url.scheme == 'https' else 'Connection is not encrypted'
    }

def check_security_headers(headers):
    """Check security headers in the response."""
    security_headers = {
        'Strict-Transport-Security': 'HSTS enforcement',
        'X-Frame-Options': 'Clickjacking protection',
        'X-Content-Type-Options': 'MIME-type sniffing protection',
        'X-XSS-Protection': 'XSS protection',
        'Content-Security-Policy': 'Content Security Policy',
        'Referrer-Policy': 'Referrer information control'
    }
    
    results = []
    for header, description in security_headers.items():
        results.append({
            'name': header,
            'status': 'secure' if header in headers else 'vulnerable',
            'details': f"{description} is {'present' if header in headers else 'missing'}"
        })
    return results

def check_rate_limiting(url):
    """Check if rate limiting is implemented."""
    attempts = 10
    rate_limited = False
    
    for _ in range(attempts):
        try:
            response = requests.get(url)
            if response.status_code in [429, 403]:
                rate_limited = True
                break
        except:
            continue
            
    return {
        'name': 'Rate Limiting',
        'status': 'secure' if rate_limited else 'vulnerable',
        'details': 'Rate limiting is enforced' if rate_limited else 'No rate limiting detected'
    }

def check_password_policy(url):
    """Check password policy implementation."""
    # This is a placeholder for actual password policy checks
    return {
        'name': 'Password Policy',
        'status': 'checking',
        'details': 'Password policy check requires manual verification'
    }

def run_all_checks(url):
    """Run all authentication security checks."""
    try:
        response = requests.get(url)
        results = {
            'https': check_https_configuration(url),
            'headers': check_security_headers(response.headers),
            'rate_limiting': check_rate_limiting(url),
            'password_policy': check_password_policy(url)
        }
        return results
    except Exception as e:
        return {
            'error': str(e),
            'status': 'error',
            'message': 'Failed to complete security checks'
        }
