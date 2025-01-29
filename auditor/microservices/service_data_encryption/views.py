from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .security_checks import (
    check_encryption_at_rest,
    check_encryption_in_transit,
    check_key_management,
    check_encryption_algorithms,
    check_tls_configuration,
    check_encryption_implementation,
    run_all_checks
)

@require_http_methods(["GET"])
def check_encryption_at_rest(request):
    """Endpoint to check encryption at rest."""
    result = check_encryption_at_rest()
    return JsonResponse(result)

@require_http_methods(["GET"])
def check_encryption_in_transit(request):
    """Endpoint to check encryption in transit."""
    result = check_encryption_in_transit()
    return JsonResponse(result)

@require_http_methods(["GET"])
def check_key_management(request):
    """Endpoint to check key management."""
    result = check_key_management()
    return JsonResponse(result)

@require_http_methods(["GET"])
def check_encryption_algorithms(request):
    """Endpoint to check encryption algorithms."""
    result = check_encryption_algorithms()
    return JsonResponse(result)

@require_http_methods(["POST"])
def check_tls_config(request):
    """Endpoint to check TLS configuration of a server."""
    try:
        data = request.POST
        hostname = data.get('hostname')
        port = int(data.get('port', 443))
        
        if not hostname:
            return JsonResponse({
                'error': 'Hostname is required'
            }, status=400)
            
        result = check_tls_configuration(hostname, port)
        return JsonResponse(result)
        
    except Exception as e:
        return JsonResponse({
            'error': str(e)
        }, status=500)

@require_http_methods(["POST"])
def test_encryption(request):
    """Endpoint to test encryption implementation."""
    try:
        data = request.POST
        test_data = data.get('data', b'test data').encode()
        algorithm = data.get('algorithm', 'AES')
        
        result = check_encryption_implementation(test_data, algorithm)
        return JsonResponse(result)
        
    except Exception as e:
        return JsonResponse({
            'error': str(e)
        }, status=500)

@require_http_methods(["GET"])
def run_encryption_checks(request):
    """Endpoint to run all encryption checks."""
    results = run_all_checks()
    return JsonResponse(results)
