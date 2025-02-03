from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from drf_yasg.utils import swagger_auto_schema
from .security_checks import check_server_settings, check_server_modules, run_all_checks

@swagger_auto_schema(
    method='get',
    operation_summary="Check Server Settings",
    operation_description="Validates server configuration settings",
    responses={200: "Server settings check results"}
)
@require_http_methods(["GET"])
def check_settings(request):
    """Endpoint to check server settings configuration."""
    result = check_server_settings(request)
    return JsonResponse(result)

@swagger_auto_schema(
    method='get',
    operation_summary="Check Server Modules",
    operation_description="Evaluates server modules configuration",
    responses={200: "Server modules check results"}
)
@require_http_methods(["GET"])
def check_modules(request):
    """Endpoint to check server modules configuration."""
    result = check_server_modules(request)
    return JsonResponse(result)