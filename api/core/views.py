from rest_framework import status, views
from rest_framework.response import Response

import api


class VersionView(views.APIView):
    def get(self, request, *args, **kwargs):
        return Response({"version": api.__version__})


class HealthCheckView(views.APIView):
    def get(self, request, *args, **kwargs):
        return Response(status=status.HTTP_200_OK)
