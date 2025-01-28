from django.http import HttpResponse, JsonResponse
from .security_checks import verify_ssl_certificate


def index(request):
    return HttpResponse("Service for HTTPS and Certificate Validation")

def check_ssl_certificate(request):
    url = request.GET.get('url')
    
    if not url:
        return JsonResponse({
            'status': 'error',
            'message': 'URL parameter is required'
        }, status=400)
    
    result = verify_ssl_certificate(url)

    return JsonResponse(result)
