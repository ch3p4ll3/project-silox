from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets

from ..models.silos import Silos
from ..serializers.silos_serializer import SilosSerializer
from ...utils.influx_management import InfluxDb


class SilosViewSet(viewsets.ModelViewSet):
    queryset = Silos.objects.all()
    serializer_class = SilosSerializer
    http_method_names = ('get', 'post')
    authentication_classes = (TokenAuthentication,)

    # get all measurements
    @action(detail=True)
    def all_measurements(self, request, pk=None):
        # prendere dati da influx
        data = InfluxDb().read(pk)
        return Response(data)

    @action(detail=True)
    def last_measurement(self, request, pk=None):
        data = InfluxDb().read(pk, last=True)
        return Response(data)
