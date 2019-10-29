import logging

from rest_framework.response import Response
from rest_framework.views import APIView

logger = logging.getLogger("django")


class Home(APIView):
    def get(self, request, format=None):
        return Response({"data": "Hello"})
