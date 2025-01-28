import requests
import ssl
import socket
import datetime
from cryptography import x509
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

def get_certificate_info(url):
    # Extract the hostname from the URL
    hostname = url.replace('https://', '').replace('http://', '').split('/')[0]
    
    # Create a default SSL context
    context = ssl.create_default_context()
    
    # Get the certificate
    with socket.create_connection((hostname, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            cert = ssock.getpeercert(binary_form=True)
    
    # Load the certificate
    cert_obj = x509.load_der_x509_certificate(cert, default_backend())
    
    return cert_obj

def check_https(url):
    if url.startswith('https://'):
        return True
    return False

def check_certificate_validity(cert_obj):
    try:
        # Check if the certificate is expired
        if cert_obj.not_valid_after < datetime.datetime.utcnow():
            return False
        
        return True
    except Exception as e:
        print(f"Error checking certificate validity: {e}")
        return False

def get_certificate_issuer(cert_obj):
    try:
        # Get the certificate issuer
        issuer = cert_obj.issuer
        issuer_name = issuer.rfc4514_string()
        return issuer_name
    except Exception as e:
        print(f"Error getting certificate issuer: {e}")
        return None

def check_certificate_revocation(cert_obj):
    # Certificate revocation checks are complex and typically require a Certificate Revocation List (CRL) or Online Certificate Status Protocol (OCSP) checks.
    # For simplicity, this example does not include those checks.
    return True  # Placeholder, assume no revocation

def evaluate_https_and_certificate(url):
    if not check_https(url):
        return "The website does not use HTTPS."
    
    try:
        cert_obj = get_certificate_info(url)
        
        if not check_certificate_validity(cert_obj):
            return "The SSL/TLS certificate is expired."
        
        issuer = get_certificate_issuer(cert_obj)
        if issuer:
            print(f"Certificate Issuer: {issuer}")
        
        if not check_certificate_revocation(cert_obj):
            return "The SSL/TLS certificate is revoked."
        
        return "The website's SSL/TLS certificate is valid and HTTPS is used."
    except Exception as e:
        return f"Error evaluating HTTPS and certificate: {e}"

# Get URL input from user
website_url = input("Enter the website URL (e.g., https://example.com): ")
result = evaluate_https_and_certificate(website_url)
print(result)
