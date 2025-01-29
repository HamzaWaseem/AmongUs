from django.urls import path
from . import views

urlpatterns = [
    path('check/config/', views.check_session_config, name='check_session_config'),
    path('check/handling/', views.check_handling, name='check_handling'),
    path('check/all/', views.run_session_checks, name='run_session_checks'),
]