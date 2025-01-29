from django.urls import path
from . import views

urlpatterns = [
    path('check-versions/', views.check_dependency_versions, name='check_dependency_versions'),
    path('check-vulnerabilities/', views.check_known_vulnerabilities, name='check_known_vulnerabilities'),
    path('check-licenses/', views.check_dependency_licenses, name='check_dependency_licenses'),
    path('check-updates/', views.check_available_updates, name='check_available_updates'),
    path('run-all-checks/', views.run_dependency_checks, name='run_dependency_checks'),
]
