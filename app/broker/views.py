from django.shortcuts import render
from rest_framework.generics import ListAPIView
from . import serializers
from . import models

class BrokerView(ListAPIView):
    serializer_class = serializers.BrokerSerializer
    queryset = models.Broker.objects.all()

