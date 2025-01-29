from django.urls import path
from . import views

urlpatterns = [
    path('scan/', views.scan_xss, name='scan_xss'),
    path('report/', views.get_xss_report, name='xss_report'),
]
