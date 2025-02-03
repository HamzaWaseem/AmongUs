from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from drf_yasg.utils import swagger_auto_schema
from .security_checks import (
    check_disaster_recovery_plan,
    check_backup_procedures,
    check_system_resilience,
    run_all_checks
)

@swagger_auto_schema(
    method='get',
    operation_summary="Check Disaster Recovery",
    operation_description="Evaluates the disaster recovery plan implementation",
    responses={200: "Disaster recovery plan status"}
)
@require_http_methods(["GET"])
def check_disaster_recovery(request):
    """Endpoint to check disaster recovery plan status."""
    result = check_disaster_recovery_plan()
    return JsonResponse(result)

@swagger_auto_schema(
    method='get',
    operation_summary="Check Backup Procedures",
    operation_description="Verifies backup procedures and their implementation",
    responses={200: "Backup procedures verification results"}
)
@require_http_methods(["GET"])
def check_backups(request):
    """Endpoint to verify backup procedures."""
    result = check_backup_procedures()
    return JsonResponse(result)

@require_http_methods(["GET"])
def check_resilience(request):
    """Endpoint to evaluate system resilience."""
    result = check_system_resilience()
    return JsonResponse(result)

@require_http_methods(["GET"])
def run_business_continuity_checks(request):
    """Endpoint to run all business continuity checks."""
    results = run_all_checks()
    return JsonResponse(results)