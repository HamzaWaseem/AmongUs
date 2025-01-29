from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .security_checks import check_rate_limits, check_throttling_policies, run_all_checks

@require_http_methods(["GET"])
def check_rates(request):
    """Endpoint to check rate limiting configuration."""
    result = check_rate_limits(request)
    return JsonResponse(result)

@require_http_methods(["GET"])
def check_throttling(request):
    """Endpoint to check throttling policies."""
    result = check_throttling_policies(request)
    return JsonResponse(result)

@require_http_methods(["GET"])
def run_rate_limiting_checks(request):
    """Endpoint to run all rate limiting checks."""
    results = run_all_checks(request)
    return JsonResponse(results)