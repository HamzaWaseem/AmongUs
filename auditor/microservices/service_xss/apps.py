from django.apps import AppConfig

class ServiceXssConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'microservices.service_xss'
    verbose_name = 'XSS Protection Service'
