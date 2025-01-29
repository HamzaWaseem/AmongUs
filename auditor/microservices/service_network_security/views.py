from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .security_checks import check_network_configuration, check_ssl_tls, run_all_checks

@require_http_methods(["GET"])
def check_network(request):
    """Endpoint to check network security configuration."""
    result = check_network_configuration(request)
    return JsonResponse(result)

@require_http_methods(["GET"])
def check_ssl(request):
    """Endpoint to check SSL/TLS configuration."""
    result = check_ssl_tls(request)
    return JsonResponse(result)

@require_http_methods(["GET"])
def run_network_checks(request):
    """Endpoint to run all network security checks."""
    results = run_all_checks(request)
    return JsonResponse(results)