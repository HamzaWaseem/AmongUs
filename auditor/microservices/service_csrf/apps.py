from django.apps import AppConfig

class ServiceCsrfConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'auditor.microservices.service_csrf'
    verbose_name = 'CSRF Protection Service'
