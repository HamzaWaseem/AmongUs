from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .security_checks import (
    check_dependency_versions,
    check_known_vulnerabilities,
    check_dependency_licenses,
    check_available_updates,
    check_package_security,
    scan_requirements_file,
    run_all_checks
)

@require_http_methods(["GET"])
def check_dependency_versions(request):
    """Endpoint to check dependency versions."""
    result = check_dependency_versions()
    return JsonResponse(result)

@require_http_methods(["GET"])
def check_known_vulnerabilities(request):
    """Endpoint to check known vulnerabilities."""
    result = check_known_vulnerabilities()
    return JsonResponse(result)

@require_http_methods(["GET"])
def check_dependency_licenses(request):
    """Endpoint to check dependency licenses."""
    result = check_dependency_licenses()
    return JsonResponse(result)

@require_http_methods(["GET"])
def check_available_updates(request):
    """Endpoint to check available updates."""
    result = check_available_updates()
    return JsonResponse(result)

@require_http_methods(["POST"])
def check_package(request):
    """Endpoint to check security of a specific package."""
    try:
        data = request.POST
        package_name = data.get('package')
        version = data.get('version', 'latest')
        
        if not package_name:
            return JsonResponse({
                'error': 'Package name is required'
            }, status=400)
            
        result = check_package_security(package_name, version)
        return JsonResponse(result)
        
    except Exception as e:
        return JsonResponse({
            'error': str(e)
        }, status=500)

@require_http_methods(["POST"])
def scan_requirements(request):
    """Endpoint to scan requirements.txt file."""
    try:
        data = request.POST
        file_path = data.get('file_path', 'requirements.txt')
        
        results = scan_requirements_file(file_path)
        return JsonResponse({
            'results': results
        })
        
    except Exception as e:
        return JsonResponse({
            'error': str(e)
        }, status=500)

@require_http_methods(["GET"])
def run_dependency_checks(request):
    """Endpoint to run all dependency checks."""
    results = run_all_checks()
    return JsonResponse(results)
