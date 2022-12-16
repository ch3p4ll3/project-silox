from rest_framework.authentication import TokenAuthentication
from ..models.sensors_in_silos import SensorsInSilos

from rest_framework import viewsets

from ..serializers.sensors_in_silos_serializer import SensorsInSilosSerializer


class SensorsInSilosViewSet(viewsets.ModelViewSet):
    queryset = SensorsInSilos.objects.all()
    serializer_class = SensorsInSilosSerializer
    authentication_classes = (TokenAuthentication,)
