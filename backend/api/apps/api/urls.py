from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from .views.silos_view import SilosViewSet
from .views.liquids_view import LiquidsViewSet
from .views.logs_view import LogsViewSet
from .views.sizes_view import SizesViewSet
from .views.sensors_types_view import SensorsTypesViewSet
from .views.sensors_in_silos_view import SensorsInSilosViewSet


router = routers.DefaultRouter()
router.register('liquids', LiquidsViewSet)
router.register('silos', SilosViewSet)
router.register('logs', LogsViewSet)
router.register('sizes', SizesViewSet)
router.register('sensors', SensorsTypesViewSet)
router.register('sensors_in_silos', SensorsInSilosViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', obtain_auth_token)
]
