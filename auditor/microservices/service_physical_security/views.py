from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .security_checks import check_access_controls, check_surveillance_systems, run_all_checks

@require_http_methods(["GET"])
def check_access(request):
    """Endpoint to check physical access control systems."""
    result = check_access_controls(request)
    return JsonResponse(result)

@require_http_methods(["GET"])
def check_surveillance(request):
    """Endpoint to check surveillance systems."""
    result = check_surveillance_systems(request)
    return JsonResponse(result)

@require_http_methods(["GET"])
def run_physical_checks(request):
    """Endpoint to run all physical security checks."""
    results = run_all_checks(request)
    return JsonResponse(results)