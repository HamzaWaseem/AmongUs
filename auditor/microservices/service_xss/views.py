from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import requests
from bs4 import BeautifulSoup
import re

@require_http_methods(["POST"])
def scan_xss(request):
    try:
        data = request.POST
        target_url = data.get('url')
        
        if not target_url:
            return JsonResponse({'error': 'URL is required'}, status=400)
            
        # Fetch the page content
        response = requests.get(target_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        vulnerabilities = []
        
        # Check for potentially vulnerable input fields
        input_fields = soup.find_all(['input', 'textarea'])
        for field in input_fields:
            if field.get('type') not in ['hidden', 'submit', 'button']:
                # Check if input sanitization attributes are present
                has_sanitization = bool(field.get('pattern') or field.get('maxlength'))
                vulnerabilities.append({
                    'element': str(field),
                    'type': 'input_field',
                    'has_sanitization': has_sanitization,
                    'risk_level': 'medium' if not has_sanitization else 'low'
                })
                
        # Check for inline JavaScript
        scripts = soup.find_all('script')
        for script in scripts:
            if script.string and any(risk_pattern in script.string.lower() 
                                for risk_pattern in ['document.write', 'eval(', 'innerHTML']):
                vulnerabilities.append({
                    'element': str(script),
                    'type': 'inline_script',
                    'risk_level': 'high'
                })
                
        # Check for event handlers
        elements_with_events = soup.find_all(lambda tag: any(attr.startswith('on') 
                                                        for attr in tag.attrs))
        for element in elements_with_events:
            vulnerabilities.append({
                'element': str(element),
                'type': 'event_handler',
                'risk_level': 'medium'
            })
            
        return JsonResponse({
            'url': target_url,
            'vulnerabilities_found': len(vulnerabilities),
            'vulnerabilities': vulnerabilities,
            'status': 'success'
        })
        
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@require_http_methods(["GET"])
def get_xss_report(request):
    target_url = request.GET.get('url')
    if not target_url:
        return JsonResponse({'error': 'URL parameter is required'}, status=400)
        
    # Get the stored XSS scan results for the URL
    # This would typically come from a database, but for now we'll do a fresh scan
    result = scan_xss(request)
    
    return JsonResponse({
        'url': target_url,
        'report_generated': True,
        'findings': result.content.decode() if hasattr(result, 'content') else result
    })
