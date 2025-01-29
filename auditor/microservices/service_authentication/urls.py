from django.urls import path
from . import views

urlpatterns = [
    path('analyze/', views.analyze_auth_security, name='analyze_auth_security'),
    path('report/', views.get_auth_report, name='get_auth_report'),
]
