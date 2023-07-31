from django.urls import path, include
from app_autiste.models import autiste

from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class AutisteSerializer(serializers.ModelSerializer):
    class Meta:
        model = autiste
        fields = "__all__"