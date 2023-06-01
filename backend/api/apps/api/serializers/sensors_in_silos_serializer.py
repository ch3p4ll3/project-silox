from rest_framework import serializers
from ..models import SensorsInSilos


class SensorsInSilosSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorsInSilos
        fields = '__all__'
