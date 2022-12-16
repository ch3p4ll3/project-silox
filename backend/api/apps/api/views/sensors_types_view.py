from rest_framework.authentication import TokenAuthentication
from ..models.sensors_types import SensorsTypes

from rest_framework import viewsets

from ..serializers.sensors_types_serializer import SensorsTypesSerializer


class SensorsTypesViewSet(viewsets.ModelViewSet):
    queryset = SensorsTypes.objects.all()
    serializer_class = SensorsTypesSerializer
    authentication_classes = (TokenAuthentication,)
