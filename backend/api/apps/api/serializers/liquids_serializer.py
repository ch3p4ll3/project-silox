from rest_framework import serializers
from ..models import Liquids


class LiquidsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Liquids
        fields = ('id', 'name', 'description', 'density',
                  'pHMin', 'pHMax', 'cO2Min', 'cO2Max',
                  'tempMin', 'tempMax', 'maxPression', 'minPression')
