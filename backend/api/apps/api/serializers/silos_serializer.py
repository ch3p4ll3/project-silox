from rest_framework import serializers
from ..models.silos import Silos
from .liquids_serializer import LiquidsSerializer


class SilosSerializer(serializers.ModelSerializer):
    liquid = LiquidsSerializer(read_only=True)

    class Meta:
        model = Silos
        fields = ('id', 'name', 'height', 'diameter', 'liquid', 'lastmeasurement', 'is_worker_running')
