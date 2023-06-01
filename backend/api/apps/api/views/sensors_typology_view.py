from rest_framework.authentication import TokenAuthentication
from ..models import SensorsTypology

from rest_framework import viewsets

from ..serializers.sensors_typology_serializer import SensorsTypologySerializer


class SensorsTypologyViewSet(viewsets.ModelViewSet):
    queryset = SensorsTypology.objects.all()
    serializer_class = SensorsTypologySerializer
    authentication_classes = (TokenAuthentication,)
