from django.shortcuts import render
from rest_framework.generics import ListAPIView
import serializers
from .models import Broker


class ListBroker(ListAPIView):
    serializer_class = serializers.BrokeSerializer
    queryset = Broker.objects.all()
    