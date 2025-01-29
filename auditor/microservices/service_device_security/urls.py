from django.urls import path
from . import views

urlpatterns = [
    path('check/authentication/', views.check_authentication, name='check_authentication'),
    path('check/policies/', views.check_policies, name='check_policies'),
    path('check/all/', views.run_device_checks, name='run_device_checks'),
]