from rest_framework import serializers
from ..models import Liquids
from .liquids_properties_serializer import LiquidsPropertiesSerializer


class LiquidsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Liquids
        fields = '__all__'
