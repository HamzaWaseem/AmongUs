from django.apps import AppConfig

class ServiceAuthenticationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'microservices.service_authentication'
    verbose_name = 'Authentication Service'
