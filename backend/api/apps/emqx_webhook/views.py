from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from ..utils.influx_management import InfluxDb


class EmqxWebhoox(APIView):
    authentication_classes = (TokenAuthentication,)

    def post(self, request, format=None):
        InfluxDb().write(request.data)  # salvataggio dati su influx
        return Response()
