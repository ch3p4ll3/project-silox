from rest_framework.authentication import TokenAuthentication
from ..models import Liquids

from rest_framework import viewsets

from ..serializers.liquids_serializer import LiquidsSerializer


class LiquidsViewSet(viewsets.ModelViewSet):
    queryset = Liquids.objects.all()
    serializer_class = LiquidsSerializer
    authentication_classes = (TokenAuthentication,)
