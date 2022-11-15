from rest_framework.authentication import TokenAuthentication
from ..models.zones import Zones

from rest_framework import viewsets

from ..serializers.zone_serializer import ZonesSerializer


class ZonesViewSet(viewsets.ModelViewSet):
    queryset = Zones.objects.all()
    serializer_class = ZonesSerializer
    authentication_classes = (TokenAuthentication,)
