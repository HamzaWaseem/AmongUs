from django.urls import path
from . import views

urlpatterns = [
    path('check-authentication/', views.check_authentication, name='check_authentication'),
    path('check-rate-limits/', views.check_rate_limits, name='check_rate_limits'),
    path('check-validation/', views.check_validation, name='check_validation'),
    path('check-versioning/', views.check_versioning, name='check_versioning'),
    path('run-all-checks/', views.run_api_security_checks, name='run_api_security_checks'),
]
