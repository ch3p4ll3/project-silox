from rest_framework import serializers
from ..models import Liquids
from .liquids_properties_serializer_get import LiquidsPropertiesSerializerGet


class LiquidsSerializerGet(serializers.ModelSerializer):
    properties = LiquidsPropertiesSerializerGet(many=True, required=False)

    class Meta:
        model = Liquids
        fields = '__all__'
        depth = 2
