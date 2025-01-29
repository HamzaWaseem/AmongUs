from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .security_checks import check_policy_compliance, check_policy_enforcement, run_all_checks

@require_http_methods(["GET"])
def check_compliance(request):
    """Endpoint to check security policy compliance."""
    result = check_policy_compliance(request)
    return JsonResponse(result)

@require_http_methods(["GET"])
def check_enforcement(request):
    """Endpoint to check policy enforcement mechanisms."""
    result = check_policy_enforcement(request)
    return JsonResponse(result)

@require_http_methods(["GET"])
def run_policy_checks(request):
    """Endpoint to run all security policy checks."""
    results = run_all_checks(request)
    return JsonResponse(results)