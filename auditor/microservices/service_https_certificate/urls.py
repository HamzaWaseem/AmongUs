from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('check-ssl/', views.check_ssl, name='check_ssl'),
]
