from django.http import HttpResponse, JsonResponse
from .security_checks import validate_ssl_certificate

def index(request):
    return HttpResponse("Service for HTTPS and Certificate Validation")

def check_ssl(request):
    url = request.GET.get('url')
    if not url:
        return JsonResponse({'error': 'URL parameter is required'}, status=400)
    
    result = validate_ssl_certificate(url)
    return JsonResponse(result)
