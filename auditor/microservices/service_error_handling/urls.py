from django.urls import path
from . import views

urlpatterns = [
    path('check/logging/', views.check_logging, name='check_logging'),
    path('check/handling/', views.check_handling, name='check_handling'),
    path('check/all/', views.run_error_checks, name='run_error_checks'),
]