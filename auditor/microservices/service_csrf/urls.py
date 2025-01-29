from django.urls import path
from . import views

urlpatterns = [
    path('check-csrf/', views.check_csrf_protection, name='check_csrf_protection'),
    path('check-token/', views.check_csrf_token, name='check_csrf_token'),
    path('check-headers/', views.check_csrf_headers, name='check_csrf_headers'),
    path('run-all-checks/', views.run_csrf_security_checks, name='run_csrf_security_checks'),
]
