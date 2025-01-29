from django.apps import AppConfig

class ServiceErrorHandlingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'microservices.service_error_handling'
    verbose_name = 'Error Handling Service'
