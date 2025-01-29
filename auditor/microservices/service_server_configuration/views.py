from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .security_checks import check_server_settings, check_server_modules, run_all_checks

@require_http_methods(["GET"])
def check_settings(request):
    """Endpoint to check server settings configuration."""
    result = check_server_settings(request)
    return JsonResponse(result)

@require_http_methods(["GET"])
def check_modules(request):
    """Endpoint to check server modules configuration."""
    result = check_server_modules(request)
    return JsonResponse(result)

@require_http_methods(["GET"])
def run_server_checks(request):
    """Endpoint to run all server configuration checks."""
    results = run_all_checks(request)
    return JsonResponse(results)