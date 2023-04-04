import json

from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework import viewsets

from ..models.silos import Silos
from ..serializers.silos_serializer import SilosSerializer

from ...utils.mqtt import client


class SilosViewSet(viewsets.ModelViewSet):
    queryset = Silos.objects.all()
    serializer_class = SilosSerializer
    http_method_names = ('get', 'post', 'patch')
    authentication_classes = (TokenAuthentication,)

    @action(url_path=r'actions/fill/(?P<percentage>\d+)', detail=True)
    def fill(self, request, pk=None, percentage=100):
        try:
            silos = Silos.objects.get(id=pk)
        except Silos.DoesNotExist:
            return Response({"detail": "Silos not found"}, status=HTTP_404_NOT_FOUND)

        # mqtt publish fill
        data = json.dumps(
            {
                "percentage": int(percentage)
            }
        )
        client.publish(f't/simulator/silos/{silos.id}/command/fill', data, qos=2)

        return Response({"detail": f"filling silos#{pk}"})

    @action(url_path=r'actions/empty/(?P<percentage>\d+)', detail=True)
    def empty(self, request, pk=None, percentage=0):
        try:
            silos = Silos.objects.get(id=pk)
        except Silos.DoesNotExist:
            return Response({"detail": "Silos not found"}, status=HTTP_404_NOT_FOUND)

        # mqtt publish empty
        data = json.dumps(
            {
                "percentage": int(percentage)
            }
        )
        client.publish(f't/simulator/silos/{silos.id}/command/empty', data, qos=2)

        return Response({"detail": f"emptying silos#{pk}"})

    @action(detail=True, url_path='actions/idle')
    def idle(self, request, pk=None):
        try:
            silos = Silos.objects.get(id=pk)
        except Silos.DoesNotExist:
            return Response({"detail": "Silos not found"}, status=HTTP_404_NOT_FOUND)

        # mqtt publish stop sim
        client.publish(f't/simulator/silos/{silos.id}/command/idle', '', qos=2)

        return Response({"detail": "worker stopped"})

    @action(detail=True, url_path='actions/start_worker')
    def start_worker(self, request, pk=None):
        try:
            silos = Silos.objects.get(id=pk)
        except Silos.DoesNotExist:
            return Response({"detail": "Silos not found"}, status=HTTP_404_NOT_FOUND)

        # mqtt publish start sim
        client.publish(f't/simulator/silos/{silos.id}/command/start', '', qos=2)

        return Response()

    @action(detail=True, url_path='actions/stop_worker')
    def stop_worker(self, request, pk=None):
        try:
            silos = Silos.objects.get(id=pk)
        except Silos.DoesNotExist:
            return Response({"detail": "Silos not found"}, status=HTTP_404_NOT_FOUND)

        # mqtt publish stop sim
        client.publish(f't/simulator/silos/{silos.id}/command/stop', '', qos=2)

        return Response()

    @action(detail=True, url_path='actions/kill')
    def stop_worker(self, request, pk=None):
        try:
            silos = Silos.objects.get(id=pk)
        except Silos.DoesNotExist:
            return Response({"detail": "Silos not found"}, status=HTTP_404_NOT_FOUND)

        # mqtt publish kill
        data = json.dumps(
            {
                "kill": True
            }
        )
        client.publish(f't/simulator/silos/{silos.id}/command/kill', data, qos=2)

        return Response()
