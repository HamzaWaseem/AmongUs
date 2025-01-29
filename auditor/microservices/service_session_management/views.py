from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .security_checks import check_session_configuration, check_session_handling, run_all_checks

@require_http_methods(["GET"])
def check_session_config(request):
    """Endpoint to check session configuration."""
    result = check_session_configuration(request)
    return JsonResponse(result)

@require_http_methods(["GET"])
def check_handling(request):
    """Endpoint to check session handling."""
    result = check_session_handling(request)
    return JsonResponse(result)

@require_http_methods(["GET"])
def run_session_checks(request):
    """Endpoint to run all session management checks."""
    results = run_all_checks(request)
    return JsonResponse(results)