from django.apps import AppConfig

class ServiceAuthorizationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'microservices.service_authorization'
    verbose_name = 'Authorization Service'
