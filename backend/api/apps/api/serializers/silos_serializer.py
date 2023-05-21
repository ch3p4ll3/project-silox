from rest_framework import serializers
from ..models import Silos


class SilosSerializer(serializers.ModelSerializer):
    # liquid = LiquidsSerializer(required=False)
    # size = SizesSerializer(read_only=False, required=False)
    # sensors = SensorsInSilosSerializer(source='sensorsinsilos_set', many=True, read_only=False, required=False)

    class Meta:
        model = Silos
        fields = '__all__'
        # depth = 6
