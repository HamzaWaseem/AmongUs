from django.urls import path
from . import views

urlpatterns = [
    path('check/rbac/', views.check_rbac, name='check_rbac'),
    path('check/permissions/', views.check_permissions, name='check_permissions'),
    path('check/tokens/', views.validate_tokens, name='validate_tokens'),
    path('check/policies/', views.check_policies, name='check_policies'),
    path('check/all/', views.run_authorization_checks, name='run_authorization_checks'),
]