import json

from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets

from ..models import Silos, Logs
from ..serializers.silos_serializer import SilosSerializer
from ..serializers.size_serializer import SizesSerializer
from ..serializers.liquids_serializer import LiquidsSerializer
from ..serializers.sensors_types_serializer import SensorsTypesSerializer

from django.shortcuts import get_object_or_404

from ...utils.mqtt import client

from logging import getLogger

logger = getLogger(__name__)


class SilosViewSet(viewsets.ModelViewSet):
    queryset = Silos.objects.all()
    serializer_class = SilosSerializer
    http_method_names = ('get', 'post', 'patch', 'delete', 'put')
    authentication_classes = (TokenAuthentication,)

    @action(url_path=r'actions/fill/(?P<percentage>\d+)', detail=True)
    def fill(self, request, pk=None, percentage=100):
        silos = get_object_or_404(Silos, id=pk)

        logger.info(f"filling silos#{pk}")

        # mqtt publish fill
        data = json.dumps(
            {
                "id": silos.id,
                "percentage": int(percentage)
            }
        )
        Logs.add_log("fill", "filling silos", silos)
        client.publish(f't/simulator/silos/{silos.id}/command/fill', data, qos=2)

        return Response({"detail": f"filling silos#{pk}"})

    @action(url_path=r'actions/empty/(?P<percentage>\d+)', detail=True)
    def empty(self, request, pk=None, percentage=0):
        silos = get_object_or_404(Silos, id=pk)

        logger.info(f"emptying silos#{pk}")

        # mqtt publish empty
        data = json.dumps(
            {
                "id": silos.id,
                "percentage": int(percentage)
            }
        )
        Logs.add_log("empty", "emptying silos", silos)
        client.publish(f't/simulator/silos/{silos.id}/command/empty', data, qos=2)

        return Response({"detail": f"emptying silos#{pk}"})

    @action(detail=True, url_path='actions/idle')
    def idle(self, request, pk=None):
        silos = get_object_or_404(Silos, id=pk)

        logger.info(f"idle silos#{pk}")

        data = {
            "id": silos.id
        }

        # mqtt publish stop sim
        Logs.add_log("idle", "idle", silos)
        client.publish(f't/simulator/silos/{silos.id}/command/idle', json.dumps(data), qos=2)

        return Response({"detail": "worker stopped"})

    @action(detail=True, url_path='actions/start_worker')
    def start_worker(self, request, pk=None):
        silos = get_object_or_404(Silos, id=pk)

        logger.info(f"starting worker#{pk}")

        # mqtt publish start sim
        silos.status = True
        silos.save()

        data = SilosSerializer(silos).data

        data['size'] = SizesSerializer(silos.size).data
        data['liquid'] = LiquidsSerializer(silos.liquid).data
        data['sensors'] = SensorsTypesSerializer(silos.sensors.all(), many=True).data

        Logs.add_log("start worker", "starting worker", silos)
        client.publish(f't/simulator/silos/{silos.id}/command/start', json.dumps(data), qos=2)

        return Response()

    @action(detail=True, url_path='actions/stop_worker')
    def stop_worker(self, request, pk=None):
        silos = get_object_or_404(Silos, id=pk)

        logger.info(f"stopping worker#{pk}")

        silos.status = False
        silos.save()

        data = {
            "id": silos.id
        }

        # mqtt publish stop sim
        Logs.add_log("stop", "stopping worker", silos)
        client.publish(f't/simulator/silos/{silos.id}/command/stop', json.dumps(data), qos=2)

        return Response()

    @action(detail=True, url_path='actions/kill')
    def kill_worker(self, request, pk=None):
        silos = get_object_or_404(Silos, id=pk)
        
        logger.info(f"killing worker#{pk}")

        # mqtt publish kill
        data = json.dumps(
            {
                "id": silos.id,
                "kill": True
            }
        )

        Logs.add_log("kill", "killing silos", silos)
        client.publish(f't/simulator/silos/{silos.id}/command/kill', data, qos=2)

        return Response()
