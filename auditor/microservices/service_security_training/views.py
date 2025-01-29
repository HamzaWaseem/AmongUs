from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .security_checks import check_training_programs, check_awareness_campaigns, run_all_checks

@require_http_methods(["GET"])
def check_training(request):
    """Endpoint to check security training programs."""
    result = check_training_programs(request)
    return JsonResponse(result)

@require_http_methods(["GET"])
def check_awareness(request):
    """Endpoint to check security awareness campaigns."""
    result = check_awareness_campaigns(request)
    return JsonResponse(result)

@require_http_methods(["GET"])
def run_training_checks(request):
    """Endpoint to run all security training checks."""
    results = run_all_checks(request)
    return JsonResponse(results)