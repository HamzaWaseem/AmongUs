from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import requests
from urllib.parse import urlparse
import re

@require_http_methods(["POST"])
def analyze_auth_security(request):
    try:
        data = request.POST
        target_url = data.get('url')
        login_endpoint = data.get('login_endpoint', '/login')
        
        if not target_url:
            return JsonResponse({'error': 'URL is required'}, status=400)
            
        # Parse the URL to ensure it's valid
        parsed_url = urlparse(target_url)
        if not parsed_url.scheme or not parsed_url.netloc:
            return JsonResponse({'error': 'Invalid URL format'}, status=400)
            
        base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
        login_url = f"{base_url}{login_endpoint}"
        
        security_checks = []
        
        # Check HTTPS
        security_checks.append({
            'check': 'HTTPS',
            'status': 'secure' if parsed_url.scheme == 'https' else 'vulnerable',
            'description': 'Connection is encrypted' if parsed_url.scheme == 'https' 
                         else 'Connection is not encrypted'
        })
        
        # Check for basic security headers
        response = requests.get(base_url)
        headers = response.headers
        
        # Check for security headers
        security_headers = {
            'Strict-Transport-Security': 'HSTS is enforced',
            'X-Frame-Options': 'Clickjacking protection',
            'X-Content-Type-Options': 'MIME-type sniffing protection',
            'X-XSS-Protection': 'XSS protection',
        }
        
        for header, description in security_headers.items():
            security_checks.append({
                'check': header,
                'status': 'secure' if header in headers else 'vulnerable',
                'description': f"{description} is {'present' if header in headers else 'missing'}"
            })
            
        # Test for rate limiting
        rate_limit_detected = False
        for _ in range(10):
            response = requests.get(login_url)
            if response.status_code in [429, 403]:
                rate_limit_detected = True
                break
                
        security_checks.append({
            'check': 'Rate Limiting',
            'status': 'secure' if rate_limit_detected else 'vulnerable',
            'description': 'Rate limiting is enforced' if rate_limit_detected 
                        else 'No rate limiting detected'
        })
        
        return JsonResponse({
            'url': target_url,
            'security_checks': security_checks,
            'overall_status': 'secure' if all(check['status'] == 'secure' 
                                            for check in security_checks) else 'vulnerable',
            'status': 'success'
        })
        
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@require_http_methods(["GET"])
def get_auth_report(request):
    target_url = request.GET.get('url')
    if not target_url:
        return JsonResponse({'error': 'URL parameter is required'}, status=400)
        
    # Get the stored authentication security analysis results for the URL
    # This would typically come from a database, but for now we'll do a fresh analysis
    result = analyze_auth_security(request)
    
    return JsonResponse({
        'url': target_url,
        'report_generated': True,
        'findings': result.content.decode() if hasattr(result, 'content') else result
    })
