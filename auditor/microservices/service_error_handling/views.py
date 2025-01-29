from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .security_checks import check_error_logging, check_error_handling_policies, run_all_checks

@require_http_methods(["GET"])
def check_logging(request):
    """Endpoint to check error logging configuration."""
    result = check_error_logging(request)
    return JsonResponse(result)

@require_http_methods(["GET"])
def check_handling(request):
    """Endpoint to check error handling policies."""
    result = check_error_handling_policies(request)
    return JsonResponse(result)

@require_http_methods(["GET"])
def run_error_checks(request):
    """Endpoint to run all error handling checks."""
    results = run_all_checks(request)
    return JsonResponse(results)