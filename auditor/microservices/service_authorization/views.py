from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .security_checks import (
    check_rbac_configuration,
    check_permission_management,
    check_token_validation,
    check_access_policies,
    run_all_checks
)

@require_http_methods(["GET"])
def check_rbac(request):
    """Endpoint to check RBAC configuration."""
    result = check_rbac_configuration()
    return JsonResponse(result)

@require_http_methods(["GET"])
def check_permissions(request):
    """Endpoint to verify permission management."""
    result = check_permission_management()
    return JsonResponse(result)

@require_http_methods(["GET"])
def validate_tokens(request):
    """Endpoint to check token validation."""
    result = check_token_validation()
    return JsonResponse(result)

@require_http_methods(["GET"])
def check_policies(request):
    """Endpoint to verify access policies."""
    result = check_access_policies()
    return JsonResponse(result)

@require_http_methods(["GET"])
def run_authorization_checks(request):
    """Endpoint to run all authorization checks."""
    results = run_all_checks()
    return JsonResponse(results)