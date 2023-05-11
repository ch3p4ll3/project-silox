from rest_framework import serializers
from ..models import Liquids
from .liquids_properties_serializer import LiquidsPropertiesSerializer


class LiquidsSerializer(serializers.ModelSerializer):
    properties = LiquidsPropertiesSerializer(many=True, required=False)

    class Meta:
        model = Liquids
        fields = ('id', 'name', 'description', 'density', 'properties')
