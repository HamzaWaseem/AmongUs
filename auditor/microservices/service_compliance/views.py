from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .security_checks import (
    check_gdpr_compliance,
    check_hipaa_compliance,
    check_pci_compliance,
    check_sox_compliance,
    check_compliance_requirements,
    run_all_checks
)

@swagger_auto_schema(
    method='get',
    operation_summary="Check GDPR Compliance",
    operation_description="Evaluates system compliance with GDPR requirements",
    responses={200: "GDPR compliance check results"}
)
@require_http_methods(["GET"])
def check_gdpr_compliance(request):
    """Endpoint to check GDPR compliance."""
    result = check_gdpr_compliance()
    return JsonResponse(result)

@swagger_auto_schema(
    method='post',
    operation_summary="Check Specific Compliance Framework",
    operation_description="Validates compliance against a specified framework",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['framework'],
        properties={
            'framework': openapi.Schema(type=openapi.TYPE_STRING, description="Name of the compliance framework")
        }
    ),
    responses={
        200: "Compliance check results",
        400: "Invalid framework specified",
        500: "Internal server error"
    }
)
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
