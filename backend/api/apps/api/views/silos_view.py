from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework import viewsets

from ..models.silos import Silos
from ..serializers.silos_serializer import SilosSerializer
from ...utils.influx_management import InfluxDb
from ...utils.worker import Worker

from django.conf import settings


class SilosViewSet(viewsets.ModelViewSet):
    queryset = Silos.objects.all()
    serializer_class = SilosSerializer
    http_method_names = ('get', 'post', 'patch')
    authentication_classes = (TokenAuthentication,)

    # get all measurements
    @action(detail=True)
    def all_measurements(self, request, pk=None):
        # prendere dati da influx
        try:
            silos = Silos.objects.get(id=pk)
        except Silos.DoesNotExist:
            return Response({"detail": "Silos not found"}, status=HTTP_404_NOT_FOUND)

        data = InfluxDb().read(silos)
        return Response(data)

    @action(detail=True)
    def last_measurement(self, request, pk=None):
        try:
            silos = Silos.objects.get(id=pk)
        except Silos.DoesNotExist:
            return Response({"detail": "Silos not found"}, status=HTTP_404_NOT_FOUND)

        data = InfluxDb().read(silos, last=True)
        return Response(data)

    @action(url_path='actions/fill', detail=True)
    def fill(self, request, pk=None):
        try:
            silos = Silos.objects.get(id=pk)
        except Silos.DoesNotExist:
            return Response({"detail": "Silos not found"}, status=HTTP_404_NOT_FOUND)

        worker = next((i for i in settings.SIMS if i.silos), None)

        if worker is None:
            worker = Worker(silos)
            settings.SIMS.append(worker)

        worker.fill()

        return Response({"detail": f"filling silos#{pk}"})

    @action(url_path='actions/empty', detail=True)
    def unload(self, request, pk=None):
        try:
            silos = Silos.objects.get(id=pk)
        except Silos.DoesNotExist:
            return Response({"detail": "Silos not found"}, status=HTTP_404_NOT_FOUND)

        worker = next((i for i in settings.SIMS if i.silos), None)

        if worker is None:
            worker = Worker(silos)
            settings.SIMS.append(worker)

        worker.empty()

        return Response({"detail": f"emptying silos#{pk}"})

    @action(detail=True, url_path='actions/stop')
    def last_measurement(self, request, pk=None):
        try:
            silos = Silos.objects.get(id=pk)
        except Silos.DoesNotExist:
            return Response({"detail": "Silos not found"}, status=HTTP_404_NOT_FOUND)

        worker = next((i for i in settings.SIMS if i.silos), None)

        if worker is not None:
            worker.stop()

        return Response({"detail": "worker stopped"})
