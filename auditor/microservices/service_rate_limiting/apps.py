from django.apps import AppConfig

class ServiceRateLimitingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'microservices.service_rate_limiting'
    verbose_name = 'Rate Limiting Service'
