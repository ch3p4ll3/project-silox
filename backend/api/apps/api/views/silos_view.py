from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST
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

    @action(url_path=r'actions/fill/(?P<percentage>\d+)', detail=True)
    def fill(self, request, pk=None, percentage=100):
        try:
            silos = Silos.objects.get(id=pk)
        except Silos.DoesNotExist:
            return Response({"detail": "Silos not found"}, status=HTTP_404_NOT_FOUND)

        worker = next((i for i in settings.SIMS if i.silos.id == silos.id), None)

        if worker is None:
            return Response({"detail": "Worker not started"}, status=HTTP_404_NOT_FOUND)

        worker.fill(100 - int(percentage))

        return Response({"detail": f"filling silos#{pk}"})

    @action(url_path=r'actions/empty/(?P<percentage>\d+)', detail=True)
    def empty(self, request, pk=None, percentage=0):
        try:
            silos = Silos.objects.get(id=pk)
        except Silos.DoesNotExist:
            return Response({"detail": "Silos not found"}, status=HTTP_404_NOT_FOUND)

        worker = next((i for i in settings.SIMS if i.silos.id == silos.id), None)

        if worker is None:
            return Response({"detail": "Worker not started"}, status=HTTP_404_NOT_FOUND)

        worker.empty(int(percentage))

        return Response({"detail": f"emptying silos#{pk}"})

    @action(detail=True, url_path='actions/stop')
    def stop(self, request, pk=None):
        try:
            silos = Silos.objects.get(id=pk)
        except Silos.DoesNotExist:
            return Response({"detail": "Silos not found"}, status=HTTP_404_NOT_FOUND)

        worker = next((i for i in settings.SIMS if i.silos.id == silos.id), None)

        if worker is None:
            return Response({"detail": "Worker not started"}, status=HTTP_404_NOT_FOUND)

        worker.stop()

        return Response({"detail": "worker stopped"})

    @action(detail=True, url_path='actions/start_worker')
    def start_worker(self, request, pk=None):
        try:
            silos = Silos.objects.get(id=pk)
        except Silos.DoesNotExist:
            return Response({"detail": "Silos not found"}, status=HTTP_404_NOT_FOUND)

        worker = next((i for i in settings.SIMS if i.silos.id == silos.id), None)

        if worker is not None:
            return Response({"detail": "Worker already started"}, status=HTTP_400_BAD_REQUEST)

        worker = Worker(silos)
        settings.SIMS.append(worker)
        worker.start()

        return Response()

    @action(detail=True, url_path='actions/stop_worker')
    def stop_worker(self, request, pk=None):
        try:
            silos = Silos.objects.get(id=pk)
        except Silos.DoesNotExist:
            return Response({"detail": "Silos not found"}, status=HTTP_404_NOT_FOUND)

        worker = next((i for i in settings.SIMS if i.silos.id == silos.id), None)

        if worker is None:
            return Response({"detail": "Worker not started"}, status=HTTP_404_NOT_FOUND)

        worker.stop_worker()
        settings.SIMS.remove(worker)

        return Response()

    @action(detail=True, url_path='actions/status')
    def is_running(self, request, pk=None):
        try:
            silos = Silos.objects.get(id=pk)
        except Silos.DoesNotExist:
            return Response({"detail": "Silos not found"}, status=HTTP_404_NOT_FOUND)

        worker = next((i for i in settings.SIMS if i.silos.id == silos.id), None)

        return Response({"is_running": worker is not None})
