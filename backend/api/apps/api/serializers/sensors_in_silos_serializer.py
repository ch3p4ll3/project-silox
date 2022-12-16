from rest_framework import serializers
from ..models.sensors_in_silos import SensorsInSilos
from .sensors_types_serializer import SensorsTypesSerializer


class SensorsInSilosSerializer(serializers.ModelSerializer):
    sensor = SensorsTypesSerializer(read_only=True)

    class Meta:
        model = SensorsInSilos
        fields = ('sensor', 'last_maintenance', 'position')
