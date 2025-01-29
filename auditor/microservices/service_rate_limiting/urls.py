from django.urls import path
from . import views

urlpatterns = [
    path('check/rates/', views.check_rates, name='check_rates'),
    path('check/throttling/', views.check_throttling, name='check_throttling'),
    path('check/all/', views.run_rate_limiting_checks, name='run_rate_limiting_checks'),
]