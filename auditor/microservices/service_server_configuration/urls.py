from django.urls import path
from . import views

urlpatterns = [
    path('check/settings/', views.check_settings, name='check_settings'),
    path('check/modules/', views.check_modules, name='check_modules'),
    path('check/all/', views.run_server_checks, name='run_server_checks'),
]