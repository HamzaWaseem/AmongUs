from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('orchestrator.urls')),  # Changed to root path since orchestrator will handle all services
]