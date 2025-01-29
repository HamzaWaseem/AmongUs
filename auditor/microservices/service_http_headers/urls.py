from django.urls import path
from . import views

urlpatterns = [
    path('check/headers/', views.check_headers, name='check_headers'),
    path('check/custom/', views.check_custom, name='check_custom'),
    path('check/all/', views.run_header_checks, name='run_header_checks'),
]