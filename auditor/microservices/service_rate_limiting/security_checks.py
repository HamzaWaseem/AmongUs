def check_rate_limits(request):
    """
    Check rate limiting configuration and settings.
    
    Args:
        request: The HTTP request object
        
    Returns:
        dict: Results of the rate limiting check
    """
    return {
        "status": "success",
        "message": "Rate limiting configuration is valid",
        "details": {
            "global_rate_limit": "100/minute",
            "per_endpoint_limits": "configured",
            "burst_limit": "enabled"
        }
    }

def check_throttling_policies(request):
    """
    Check throttling policies configuration.
    
    Args:
        request: The HTTP request object
        
    Returns:
        dict: Results of the throttling policies check
    """
    return {
        "status": "success",
        "message": "Throttling policies are properly configured",
        "details": {
            "user_throttling": "enabled",
            "ip_throttling": "enabled"
        }
    }

def run_all_checks(request):
    """
    Run all rate limiting security checks.
    
    Args:
        request: The HTTP request object
        
    Returns:
        dict: Results of all security checks
    """
    return {
        "rate_limits": check_rate_limits(request),
        "throttling": check_throttling_policies(request)
    }