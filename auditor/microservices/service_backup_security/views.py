from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .security_checks import (
    check_backup_encryption,
    check_backup_integrity,
    check_retention_policy,
    check_access_controls,
    run_all_checks
)

@require_http_methods(["GET"])
def check_encryption(request):
    """Endpoint to check backup encryption configuration."""
    result = check_backup_encryption()
    return JsonResponse(result)

@require_http_methods(["GET"])
def check_integrity(request):
    """Endpoint to verify backup integrity checks."""
    result = check_backup_integrity()
    return JsonResponse(result)

@require_http_methods(["GET"])
def check_retention(request):
    """Endpoint to check backup retention policies."""
    result = check_retention_policy()
    return JsonResponse(result)

@require_http_methods(["GET"])
def check_access(request):
    """Endpoint to verify backup access controls."""
    result = check_access_controls()
    return JsonResponse(result)

@require_http_methods(["GET"])
def run_backup_security_checks(request):
    """Endpoint to run all backup security checks."""
    results = run_all_checks()
    return JsonResponse(results)