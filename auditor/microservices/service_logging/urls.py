from django.urls import path
from . import views

urlpatterns = [
    path('check/logging/', views.check_logging, name='check_logging'),
    path('check/audits/', views.check_audits, name='check_audits'),
    path('check/all/', views.run_logging_checks, name='run_logging_checks'),
]