from django.urls import path
from . import views

urlpatterns = [
    path('check/training/', views.check_training, name='check_training'),
    path('check/awareness/', views.check_awareness, name='check_awareness'),
    path('check/all/', views.run_training_checks, name='run_training_checks'),
]