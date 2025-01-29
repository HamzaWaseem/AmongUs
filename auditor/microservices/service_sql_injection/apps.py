from django.apps import AppConfig

class ServiceSqlInjectionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'microservices.service_sql_injection'
    verbose_name = 'SQL Injection Protection Service'
