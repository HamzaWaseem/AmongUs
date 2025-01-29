from django.urls import path
from . import views

urlpatterns = [
    path('check/compliance/', views.check_compliance, name='check_compliance'),
    path('check/enforcement/', views.check_enforcement, name='check_enforcement'),
    path('check/all/', views.run_policy_checks, name='run_policy_checks'),
]