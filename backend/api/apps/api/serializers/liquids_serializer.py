from rest_framework import serializers
from ..models.liquids import Liquids


class LiquidsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Liquids
        fields = ('id', 'name', 'description', 'density')
