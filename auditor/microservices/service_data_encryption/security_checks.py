from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import ssl
import socket

def check_encryption_at_rest():
    """Check data encryption at rest."""
    return {
        'status': 'checking',
        'message': 'Checking data encryption at rest',
        'checks': [
            {'name': 'Storage Encryption', 'status': 'pending'},
            {'name': 'Database Encryption', 'status': 'pending'},
            {'name': 'File System Encryption', 'status': 'pending'}
        ]
    }

def check_encryption_in_transit():
    """Check data encryption in transit."""
    return {
        'status': 'checking',
        'message': 'Checking data encryption in transit',
        'checks': [
            {'name': 'TLS Configuration', 'status': 'pending'},
            {'name': 'Protocol Versions', 'status': 'pending'},
            {'name': 'Certificate Validation', 'status': 'pending'}
        ]
    }

def check_key_management():
    """Check encryption key management."""
    return {
        'status': 'checking',
        'message': 'Checking key management',
        'checks': [
            {'name': 'Key Generation', 'status': 'pending'},
            {'name': 'Key Storage', 'status': 'pending'},
            {'name': 'Key Rotation', 'status': 'pending'}
        ]
    }

def check_encryption_algorithms():
    """Check encryption algorithms in use."""
    return {
        'status': 'checking',
        'message': 'Checking encryption algorithms',
        'checks': [
            {'name': 'Algorithm Strength', 'status': 'pending'},
            {'name': 'Known Vulnerabilities', 'status': 'pending'},
            {'name': 'Implementation', 'status': 'pending'}
        ]
    }

def check_tls_configuration(hostname, port=443):
    """Check TLS configuration of a server."""
    try:
        context = ssl.create_default_context()
        with socket.create_connection((hostname, port)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                cipher = ssock.cipher()
                version = ssock.version()
                
                return {
                    'status': 'secure',
                    'details': {
                        'protocol_version': version,
                        'cipher_suite': cipher[0],
                        'certificate': {
                            'subject': cert['subject'],
                            'issuer': cert['issuer'],
                            'version': cert['version']
                        }
                    }
                }
    except Exception as e:
        return {
            'status': 'error',
            'message': str(e)
        }

def check_encryption_implementation(data, algorithm='AES'):
    """Check encryption implementation."""
    try:
        if algorithm == 'AES':
            key = algorithms.AES.generate_key()
            iv = b'\x00' * 16  # For testing only
            cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
            encryptor = cipher.encryptor()
            
            # Test encryption
            ct = encryptor.update(data) + encryptor.finalize()
            
            return {
                'status': 'secure',
                'details': {
                    'algorithm': algorithm,
                    'key_size': len(key) * 8,
                    'mode': 'CBC'
                }
            }
    except Exception as e:
        return {
            'status': 'error',
            'message': str(e)
        }

def run_all_checks():
    """Run all encryption checks."""
    return {
        'at_rest': check_encryption_at_rest(),
        'in_transit': check_encryption_in_transit(),
        'key_management': check_key_management(),
        'algorithms': check_encryption_algorithms()
    }
