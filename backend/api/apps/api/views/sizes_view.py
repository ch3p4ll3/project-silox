from rest_framework.authentication import TokenAuthentication
from ..models import Sizes

from rest_framework import viewsets

from ..serializers.size_serializer import SizesSerializer


class SizesViewSet(viewsets.ModelViewSet):
    queryset = Sizes.objects.all()
    serializer_class = SizesSerializer
    authentication_classes = (TokenAuthentication,)
