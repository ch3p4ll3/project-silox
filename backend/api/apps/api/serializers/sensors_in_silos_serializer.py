from rest_framework import serializers
from ..models import SensorsInSilos
from .sensors_types_serializer import SensorsTypesSerializer


class SensorsInSilosSerializer(serializers.ModelSerializer):
    sensor = SensorsTypesSerializer(read_only=True)

    class Meta:
        model = SensorsInSilos
        fields = ('id', 'sensor', 'last_maintenance', 'position')
