from django.urls import path
from . import views

urlpatterns = [
    path('check-encryption/', views.check_encryption, name='check_encryption'),
    path('check-integrity/', views.check_integrity, name='check_integrity'),
    path('check-retention/', views.check_retention, name='check_retention'),
    path('check-access/', views.check_access, name='check_access'),
    path('run-all-checks/', views.run_backup_security_checks, name='run_backup_security_checks'),
]
