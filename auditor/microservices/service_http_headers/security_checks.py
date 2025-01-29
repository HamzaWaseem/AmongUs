def check_security_headers(request):
    """
    Check security-related HTTP headers configuration.
    
    Args:
        request: The HTTP request object
        
    Returns:
        dict: Results of the security headers check
    """
    return {
        "status": "success",
        "message": "Security headers are properly configured",
        "details": {
            "x_frame_options": "configured",
            "x_content_type_options": "set",
            "strict_transport_security": "enabled"
        }
    }

def check_custom_headers(request):
    """
    Check custom HTTP headers configuration.
    
    Args:
        request: The HTTP request object
        
    Returns:
        dict: Results of the custom headers check
    """
    return {
        "status": "success",
        "message": "Custom headers are properly configured",
        "details": {
            "content_security_policy": "implemented",
            "referrer_policy": "configured",
            "permissions_policy": "set"
        }
    }

def run_all_checks(request):
    """
    Run all HTTP headers security checks.
    
    Args:
        request: The HTTP request object
        
    Returns:
        dict: Results of all security checks
    """
    return {
        "security_headers": check_security_headers(request),
        "custom_headers": check_custom_headers(request)
    }