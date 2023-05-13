from rest_framework import serializers
from ..models import Silos, Sizes
from .liquids_serializer import LiquidsSerializer
from .size_serializer import SizesSerializer
from .sensors_in_silos_serializer import SensorsInSilosSerializer


class SilosSerializer(serializers.ModelSerializer):
    # liquid = LiquidsSerializer(required=False)
    # size = SizesSerializer(read_only=False, required=False)
    # sensors = SensorsInSilosSerializer(source='sensorsinsilos_set', many=True, read_only=False, required=False)

    class Meta:
        model = Silos
        fields = '__all__'
        # depth = 6
