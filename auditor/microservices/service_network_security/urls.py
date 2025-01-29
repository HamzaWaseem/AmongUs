from django.urls import path
from . import views

urlpatterns = [
    path('check/network/', views.check_network, name='check_network'),
    path('check/ssl/', views.check_ssl, name='check_ssl'),
    path('check/all/', views.run_network_checks, name='run_network_checks'),
]