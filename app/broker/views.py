from django.shortcuts import render
from rest_framework import generics
from . import serializers
from . import models


class BrokerListView(generics.ListCreateAPIView):
    serializer_class = serializers.BrokerSerializer
    queryset = models.Broker.objects.all()


class BrokerDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.BrokerSerializer
    queryset = models.Broker.objects.all()
    