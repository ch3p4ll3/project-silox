from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from .views import PropertiesViewSet, LiquidsPropertiesViewSet, LiquidsViewSet, LogsViewSet, SilosViewSet,\
    SensorsTypesViewSet, SensorsInSilosViewSet, SizesViewSet


router = routers.DefaultRouter()
router.register('liquids', LiquidsViewSet)
router.register('silos', SilosViewSet)
router.register('logs', LogsViewSet)
router.register('sizes', SizesViewSet)
router.register('sensors', SensorsTypesViewSet)
router.register('sensors_in_silos', SensorsInSilosViewSet)
router.register('properties', PropertiesViewSet)
router.register('liquid_properties', LiquidsPropertiesViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', obtain_auth_token)
]
