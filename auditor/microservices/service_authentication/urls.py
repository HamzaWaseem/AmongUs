from django.urls import path
from . import views

urlpatterns = [
    path('analyze/', views.analyze_auth_security, name='analyze_auth'),
    path('report/', views.get_auth_report, name='auth_report'),
]
