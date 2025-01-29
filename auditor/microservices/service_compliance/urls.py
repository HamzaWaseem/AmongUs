from django.urls import path
from . import views

urlpatterns = [
    path('check-gdpr/', views.check_gdpr_compliance, name='check_gdpr_compliance'),
    path('check-hipaa/', views.check_hipaa_compliance, name='check_hipaa_compliance'),
    path('check-pci/', views.check_pci_compliance, name='check_pci_compliance'),
    path('check-sox/', views.check_sox_compliance, name='check_sox_compliance'),
    path('run-all-checks/', views.run_compliance_checks, name='run_compliance_checks'),
]
