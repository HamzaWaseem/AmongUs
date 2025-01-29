from django.apps import AppConfig

class ServiceBackupSecurityConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'auditor.microservices.service_backup_security'
    verbose_name = 'Backup Security Service'
