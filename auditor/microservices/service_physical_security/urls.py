from django.urls import path
from . import views

urlpatterns = [
    path('check/access/', views.check_access, name='check_access'),
    path('check/surveillance/', views.check_surveillance, name='check_surveillance'),
    path('check/all/', views.run_physical_checks, name='run_physical_checks'),
]