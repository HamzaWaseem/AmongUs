from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .security_checks import (
    check_gdpr_compliance,
    check_hipaa_compliance,
    check_pci_compliance,
    check_sox_compliance,
    check_compliance_requirements,
    run_all_checks
)

@require_http_methods(["GET"])
def check_gdpr_compliance(request):
    """Endpoint to check GDPR compliance."""
    result = check_gdpr_compliance()
    return JsonResponse(result)

@require_http_methods(["GET"])
def check_hipaa_compliance(request):
    """Endpoint to check HIPAA compliance."""
    result = check_hipaa_compliance()
    return JsonResponse(result)

@require_http_methods(["GET"])
def check_pci_compliance(request):
    """Endpoint to check PCI DSS compliance."""
    result = check_pci_compliance()
    return JsonResponse(result)

@require_http_methods(["GET"])
def check_sox_compliance(request):
    """Endpoint to check SOX compliance."""
    result = check_sox_compliance()
    return JsonResponse(result)

@require_http_methods(["POST"])
def check_specific_compliance(request):
    """Endpoint to check compliance for a specific framework."""
    try:
        data = request.POST
        framework = data.get('framework')
        
        if not framework:
            return JsonResponse({
                'error': 'Compliance framework must be specified'
            }, status=400)
            
        result = check_compliance_requirements(framework, data)
        return JsonResponse(result)
        
    except Exception as e:
        return JsonResponse({
            'error': str(e)
        }, status=500)

@require_http_methods(["GET"])
def run_compliance_checks(request):
    """Endpoint to run all compliance checks."""
    results = run_all_checks()
    return JsonResponse(results)
