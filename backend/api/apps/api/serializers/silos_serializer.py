from rest_framework import serializers
from ..models.silos import Silos
from .zone_serializer import ZonesSerializer
from .liquids_serializer import LiquidsSerializer
from .actions_serializer import ActionsSerializer


class SilosSerializer(serializers.ModelSerializer):
    zone = ZonesSerializer(read_only=True)
    liquid = LiquidsSerializer(read_only=True)
    actions = ActionsSerializer(many=True, read_only=True)

    class Meta:
        model = Silos
        fields = ('id', 'height', 'diameter', 'zone', 'liquid', 'actions', 'lastmeasurement', 'is_worker_running')
