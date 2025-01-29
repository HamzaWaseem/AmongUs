from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .security_checks import check_device_authentication, check_device_policies, run_all_checks

@require_http_methods(["GET"])
def check_authentication(request):
    """Endpoint to check device authentication configuration."""
    result = check_device_authentication(request)
    return JsonResponse(result)

@require_http_methods(["GET"])
def check_policies(request):
    """Endpoint to check device security policies."""
    result = check_device_policies(request)
    return JsonResponse(result)

@require_http_methods(["GET"])
def run_device_checks(request):
    """Endpoint to run all device security checks."""
    results = run_all_checks(request)
    return JsonResponse(results)