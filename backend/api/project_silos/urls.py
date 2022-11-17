"""project_silos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view, openapi
from rest_framework import permissions
from django.conf import settings
from django.conf.urls.static import static

from apps.utils.worker import Worker
from apps.api.models.silos import Silos


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.api.urls')),
    path('emqx_webhook', include('apps.emqx_webhook.urls')),

    path('openapi/', get_schema_view(
        public=True,
        title="Project Silos",
        description="API for Project Silos",
        version="1.0.0",
        permission_classes=[permissions.AllowAny]
    ), name='openapi-schema'),

    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

settings.SIMS = [Worker(i) for i in Silos.objects.all()]  # usato per creare la lista di tutti i silos
