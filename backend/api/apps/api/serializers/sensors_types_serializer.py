from rest_framework import serializers
from ..models import SensorsTypes


class SensorsTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorsTypes
        fields = ('id', 'sensor_name', 'sensor_type', 'sensor_slug', 'maintenance_interval', 'min_value', 'max_value')
