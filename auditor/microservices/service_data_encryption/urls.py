from django.urls import path
from . import views

urlpatterns = [
    path('check-at-rest/', views.check_encryption_at_rest, name='check_encryption_at_rest'),
    path('check-in-transit/', views.check_encryption_in_transit, name='check_encryption_in_transit'),
    path('check-key-management/', views.check_key_management, name='check_key_management'),
    path('check-algorithms/', views.check_encryption_algorithms, name='check_encryption_algorithms'),
    path('run-all-checks/', views.run_encryption_checks, name='run_encryption_checks'),
]
