from rest_framework import serializers
from ..models.zones import Zones


class ZonesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zones
        fields = ('id', 'name', 'latitude', 'longitude')
