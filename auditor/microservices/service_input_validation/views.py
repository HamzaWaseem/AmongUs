from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .security_checks import check_input_sanitization, check_validation_rules, run_all_checks

@require_http_methods(["GET"])
def check_sanitization(request):
    """Endpoint to check input sanitization configuration."""
    result = check_input_sanitization(request)
    return JsonResponse(result)

@require_http_methods(["GET"])
def check_validation(request):
    """Endpoint to check validation rules."""
    result = check_validation_rules(request)
    return JsonResponse(result)

@require_http_methods(["GET"])
def run_validation_checks(request):
    """Endpoint to run all input validation checks."""
    results = run_all_checks(request)
    return JsonResponse(results)