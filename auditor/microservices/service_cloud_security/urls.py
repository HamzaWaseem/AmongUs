from django.urls import path
from . import views

urlpatterns = [
    path('check-iam/', views.check_iam_configuration, name='check_iam_configuration'),
    path('check-storage/', views.check_storage_security, name='check_storage_security'),
    path('check-network/', views.check_network_security, name='check_network_security'),
    path('check-monitoring/', views.check_monitoring_configuration, name='check_monitoring_configuration'),
    path('run-all-checks/', views.run_cloud_security_checks, name='run_cloud_security_checks'),
]
