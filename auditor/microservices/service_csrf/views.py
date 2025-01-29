from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import requests
from urllib.parse import urlparse
from .security_checks import (
    check_csrf_implementation,
    check_token_validation,
    check_header_configuration,
    run_all_checks
)

@require_http_methods(["POST"])
def check_csrf_protection(request):
    try:
        data = request.POST
        target_url = data.get('url')
        
        if not target_url:
            return JsonResponse({'error': 'URL is required'}, status=400)
            
        # Parse the URL to ensure it's valid
        parsed_url = urlparse(target_url)
        if not parsed_url.scheme or not parsed_url.netloc:
            return JsonResponse({'error': 'Invalid URL format'}, status=400)
            
        # Perform CSRF check
        session = requests.Session()
        
        # First request to get any CSRF token
        response = session.get(target_url)
        csrf_token = None
        
        # Check for common CSRF token names in cookies and headers
        csrf_headers = ['X-CSRFToken', 'X-CSRF-Token', '_csrf']
        for header in csrf_headers:
            if header in response.headers:
                csrf_token = response.headers[header]
                break
                
        # Attempt a POST request without CSRF token
        test_data = {'test': 'data'}
        try:
            response = session.post(target_url, data=test_data, allow_redirects=False)
            csrf_protected = response.status_code in [403, 401]
        except requests.exceptions.RequestException:
            csrf_protected = None
            
        result = {
            'url': target_url,
            'csrf_token_present': csrf_token is not None,
            'csrf_protection_detected': csrf_protected,
            'status': 'success'
        }
        
        return JsonResponse(result)
        
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@require_http_methods(["GET"])
def get_csrf_report(request):
    target_url = request.GET.get('url')
    if not target_url:
        return JsonResponse({'error': 'URL parameter is required'}, status=400)
        
    # Get the stored CSRF check results for the URL
    # This would typically come from a database, but for now we'll do a fresh check
    result = check_csrf_protection(request)
    
    return JsonResponse({
        'url': target_url,
        'report_generated': True,
        'findings': result.content.decode() if hasattr(result, 'content') else result
    })

@require_http_methods(["GET"])
def check_csrf_protection(request):
    """Endpoint to check CSRF protection implementation."""
    result = check_csrf_implementation()
    return JsonResponse(result)

@require_http_methods(["GET"])
def check_csrf_token(request):
    """Endpoint to verify CSRF token validation."""
    result = check_token_validation()
    return JsonResponse(result)

@require_http_methods(["GET"])
def check_csrf_headers(request):
    """Endpoint to check CSRF header configuration."""
    result = check_header_configuration()
    return JsonResponse(result)

@require_http_methods(["GET"])
def run_csrf_security_checks(request):
    """Endpoint to run all CSRF security checks."""
    results = run_all_checks()
    return JsonResponse(results)
