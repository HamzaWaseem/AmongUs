from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .security_checks import (
    check_api_authentication,
    check_rate_limiting,
    check_input_validation,
    check_api_versioning,
    run_all_checks
)

@require_http_methods(["GET"])
def check_authentication(request):
    """Endpoint to check API authentication configuration."""
    result = check_api_authentication()
    return JsonResponse(result)

@require_http_methods(["GET"])
def check_rate_limits(request):
    """Endpoint to verify rate limiting implementation."""
    result = check_rate_limiting()
    return JsonResponse(result)

@require_http_methods(["GET"])
def check_validation(request):
    """Endpoint to check input validation mechanisms."""
    result = check_input_validation()
    return JsonResponse(result)

@require_http_methods(["GET"])
def check_versioning(request):
    """Endpoint to verify API versioning implementation."""
    result = check_api_versioning()
    return JsonResponse(result)

@require_http_methods(["GET"])
def run_api_security_checks(request):
    """Endpoint to run all API security checks."""
    results = run_all_checks()
    return JsonResponse(results)