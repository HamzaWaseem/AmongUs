from django.urls import path
from . import views

urlpatterns = [
    path('check/sanitization/', views.check_sanitization, name='check_sanitization'),
    path('check/validation/', views.check_validation, name='check_validation'),
    path('check/all/', views.run_validation_checks, name='run_validation_checks'),
]