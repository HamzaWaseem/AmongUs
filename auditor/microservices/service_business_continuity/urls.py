from django.urls import path
from . import views

urlpatterns = [
    path('check-disaster-recovery/', views.check_disaster_recovery, name='check_disaster_recovery'),
    path('check-backups/', views.check_backups, name='check_backups'),
    path('check-resilience/', views.check_resilience, name='check_resilience'),
    path('run-all-checks/', views.run_business_continuity_checks, name='run_business_continuity_checks'),
]
