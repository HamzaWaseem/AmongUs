import ssl
import socket
from datetime import datetime

import certifi
from urllib.parse import urlparse

def verify_ssl_certificate(url):

    try:
        # Parse the URL to get the hostname
        parsed_url = urlparse(url)
        hostname = parsed_url.netloc
        if not hostname:
            hostname = url

        # Remove port if present
        hostname = hostname.split(':')[0]
        
        # Create SSL context using certifi for trusted certificates
        context = ssl.create_default_context(cafile=certifi.where())

        
        with socket.create_connection((hostname, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                
                # Get certificate expiration date
                expire_date = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y GMT')
                current_date = datetime.utcnow()
                
                return {
                    'status': 'valid',
                    'expires': expire_date.strftime('%Y-%m-%d %H:%M:%S'),
                    'issuer': dict(x[0] for x in cert['issuer']),
                    'subject': dict(x[0] for x in cert['subject']),
                    'days_remaining': (expire_date - current_date).days
                }
                
    except ssl.SSLCertVerificationError:
        return {'status': 'invalid', 'error': 'Certificate verification failed'}
    except ssl.SSLError:
        return {'status': 'invalid', 'error': 'SSL error occurred'}
    except socket.gaierror:
        return {'status': 'invalid', 'error': 'Could not resolve hostname'}
    except Exception as e:
        return {'status': 'invalid', 'error': str(e)}

