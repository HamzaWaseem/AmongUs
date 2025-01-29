from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('orchestrator/', include('orchestrator.urls')),
    path('service_https_certificate/', include('microservices.service_https_certificate.urls')),
    path('service_csrf/', include('microservices.service_csrf.urls')),
    path('service_xss/', include('microservices.service_xss.urls')),
    path('service_authentication/', include('microservices.service_authentication.urls')),
] 