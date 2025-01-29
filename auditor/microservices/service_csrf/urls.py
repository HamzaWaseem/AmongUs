from django.urls import path
from . import views

urlpatterns = [
    path('check/', views.check_csrf_protection, name='check_csrf'),
    path('report/', views.get_csrf_report, name='csrf_report'),
]
