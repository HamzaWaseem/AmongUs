from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .security_checks import check_logging_configuration, check_audit_trails, run_all_checks

@require_http_methods(["GET"])
def check_logging(request):
    """Endpoint to check logging configuration."""
    result = check_logging_configuration(request)
    return JsonResponse(result)

@require_http_methods(["GET"])
def check_audits(request):
    """Endpoint to check audit trail configuration."""
    result = check_audit_trails(request)
    return JsonResponse(result)

@require_http_methods(["GET"])
def run_logging_checks(request):
    """Endpoint to run all logging checks."""
    results = run_all_checks(request)
    return JsonResponse(results)