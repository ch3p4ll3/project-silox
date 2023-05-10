from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from ..models import Logs, Silos
from ..serializers.logs_serializer import LogsSerializer
from django.shortcuts import get_object_or_404


class LogsViewSet(viewsets.ModelViewSet):
    queryset = Logs.objects.all()
    serializer_class = LogsSerializer
    http_method_names = ('get',)
    authentication_classes = (TokenAuthentication,)

    @action(url_path=r'(?P<silos_id>\w+)/last/(?P<logs_number>\w+)', detail=False)
    def last_silos_log(self, request, silos_id, logs_number):
        silos = get_object_or_404(Silos, id=silos_id)

        last_log = Logs.get_by_silos(silos, int(logs_number))
        return Response(LogsSerializer(last_log, many=True).data)
