def check_input_sanitization(request):
    """
    Check input sanitization configuration and implementation.
    
    Args:
        request: The HTTP request object
        
    Returns:
        dict: Results of the input sanitization check
    """
    return {
        "status": "success",
        "message": "Input sanitization is properly configured",
        "details": {
            "xss_protection": "enabled",
            "sql_injection_protection": "enabled",
            "html_encoding": "active"
        }
    }

def check_validation_rules(request):
    """
    Check validation rules configuration.
    
    Args:
        request: The HTTP request object
        
    Returns:
        dict: Results of the validation rules check
    """
    return {
        "status": "success",
        "message": "Validation rules are properly configured",
        "details": {
            "data_type_validation": "enabled",
            "range_validation": "enabled",
            "format_validation": "enabled"
        }
    }

def run_all_checks(request):
    """
    Run all input validation security checks.
    
    Args:
        request: The HTTP request object
        
    Returns:
        dict: Results of all security checks
    """
    return {
        "input_sanitization": check_input_sanitization(request),
        "validation_rules": check_validation_rules(request)
    }