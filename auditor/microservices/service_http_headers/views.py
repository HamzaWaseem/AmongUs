from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .security_checks import check_security_headers, check_custom_headers, run_all_checks

@require_http_methods(["GET"])
def check_headers(request):
    """Endpoint to check security headers configuration."""
    result = check_security_headers(request)
    return JsonResponse(result)

@require_http_methods(["GET"])
def check_custom(request):
    """Endpoint to check custom headers configuration."""
    result = check_custom_headers(request)
    return JsonResponse(result)

@require_http_methods(["GET"])
def run_header_checks(request):
    """Endpoint to run all HTTP headers checks."""
    results = run_all_checks(request)
    return JsonResponse(results)