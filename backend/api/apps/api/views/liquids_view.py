from rest_framework.authentication import TokenAuthentication
from ..models import Liquids

from rest_framework import viewsets

from ..serializers.liquids_serializer import LiquidsSerializer
from ..serializers.liquids_serializer_get import LiquidsSerializerGet


class LiquidsViewSet(viewsets.ModelViewSet):
    queryset = Liquids.objects.all()
    serializer_class = LiquidsSerializer
    authentication_classes = (TokenAuthentication,)

    def get_serializer_class(self):
        if self.request and self.request.method != 'GET':
            return LiquidsSerializer
        return LiquidsSerializerGet
