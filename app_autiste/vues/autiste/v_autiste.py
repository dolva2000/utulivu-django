from django.urls import path, include
from app_autiste.models import autiste
from app_autiste.vues.autiste.sz_autiste import AutisteSerializer

from rest_framework import routers, serializers, viewsets


# ViewSets define the view behavior.
class AutisteViewSet(viewsets.ModelViewSet):
    queryset = autiste.objects.all()
    serializer_class = AutisteSerializer