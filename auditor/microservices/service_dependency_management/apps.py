from django.apps import AppConfig

class ServiceDependencyManagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'auditor.microservices.service_dependency_management'
    verbose_name = 'Dependency Management Service'
