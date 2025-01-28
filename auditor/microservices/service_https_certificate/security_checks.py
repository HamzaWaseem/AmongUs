import ssl
import socket
from datetime import datetime
from urllib.parse import urlparse

def validate_ssl_certificate(url):
    try:
        # Parse the URL to get the hostname
        parsed_url = urlparse(url)
        hostname = parsed_url.netloc
        if not hostname:
            hostname = url

        # Create SSL context
        context = ssl.create_default_context()
        
        with socket.create_connection((hostname, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                
                # Get certificate expiration date
                exp_date = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y GMT')
                current_date = datetime.utcnow()
                
                return {
                    'valid': True,
                    'expires': exp_date.strftime('%Y-%m-%d %H:%M:%S'),
                    'issuer': dict(x[0] for x in cert['issuer']),
                    'subject': dict(x[0] for x in cert['subject'])
                }

    except Exception as e:
        return {
            'valid': False,
            'error': str(e)
        }