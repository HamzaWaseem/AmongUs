from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('orchestrator/', include('microservices.orchestrator.urls')),
    path('service_https_certificate/', include('microservices.service_https_certificate.urls')),
] 