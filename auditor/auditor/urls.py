"""
URL configuration for auditor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('orchestrator/', include('orchestrator.urls')),
    path('service_https_certificate/', include('microservices.service_https_certificate.urls')),
    # path('service_xss/', include('microservices.service_xss.urls')),
    # path('service_sql_injection/', include('microservices.service_sql_injection.urls')),
    # path('service_csrf/', include('microservices.service_csrf.urls')),
    # path('service_authentication/', include('microservices.service_authentication.urls')),
    # path('service_authorization/', include('microservices.service_authorization.urls')),
    # path('service_rate_limiting/', include('microservices.service_rate_limiting.urls')),
    # path('service_input_validation/', include('microservices.service_input_validation.urls')),
    # path('service_error_handling/', include('microservices.service_error_handling.urls')),
    # path('service_logging/', include('microservices.service_logging.urls')),
    # path('service_data_encryption/', include('microservices.service_data_encryption.urls')),
    # path('service_session_management/', include('microservices.service_session_management.urls')),
    # path('service_http_headers/', include('microservices.service_http_headers.urls')),
    # path('service_dependency_management/', include('microservices.service_dependency_management.urls')),
    # path('service_server_configuration/', include('microservices.service_server_configuration.urls')),
    # path('service_cloud_security/', include('microservices.service_cloud_security.urls')),
    # path('service_api_security/', include('microservices.service_api_security.urls')),
    # path('service_backup_security/', include('microservices.service_backup_security.urls')),
    # path('service_network_security/', include('microservices.service_network_security.urls')),
    # path('service_device_security/', include('microservices.service_device_security.urls')),
    # path('service_physical_security/', include('microservices.service_physical_security.urls')),
    # path('service_business_continuity/', include('microservices.service_business_continuity.urls')),
    # path('service_vulnerability_management/', include('microservices.service_vulnerability_management.urls')),
    # path('service_compliance/', include('microservices.service_compliance.urls')),
    # path('service_security_training/', include('microservices.service_security_training.urls')),
    # path('service_security_policies/', include('microservices.service_security_policies.urls')),
]

