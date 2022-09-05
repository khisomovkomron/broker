from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import \
    IsAuthenticated, \
    IsAuthenticatedOrReadOnly
from . import serializers
from . import models
from drf_spectacular.utils import (
    extend_schema_view,
    extend_schema,
    OpenApiParameter,
    OpenApiTypes,
)


class BrokerListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = serializers.BrokerSerializer
    queryset = models.Broker.objects.all()

class BrokerDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.BrokerSerializer
    queryset = models.Broker.objects.all()
    