import sys
import os

# Add the project base directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'security_django_project.settings'

# Now you can import your microservices
from microservices.service_https_certificate.security_checks import perform_security_checks as https_checks
from microservices.service_xss.security_checks import perform_security_checks as xss_checks
from microservices.service_sql_injection.security_checks import perform_security_checks as sql_injection_checks
# Add similar imports for other services

def run_all_checks():
    # Example URL
    url = 'https://example.com'
    
    print("Running HTTPS and Certificate Validation Checks")
    https_checks(url)
    
    print("Running XSS Checks")
    xss_checks(url)
    
    print("Running SQL Injection Checks")
    sql_injection_checks(url)
    
    # Add similar calls for other services

if __name__ == "__main__":
    run_all_checks()
