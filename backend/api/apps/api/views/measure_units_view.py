from rest_framework.authentication import TokenAuthentication
from ..models import MeasureUnits

from rest_framework import viewsets

from ..serializers.measure_units_serializer import MeasureUnitsSerializer


class MeasureUnitsViewSet(viewsets.ModelViewSet):
    queryset = MeasureUnits.objects.all()
    serializer_class = MeasureUnitsSerializer
    authentication_classes = (TokenAuthentication,)
