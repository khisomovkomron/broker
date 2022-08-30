from django.shortcuts import render
from rest_framework.generics import ListAPIView
from serializers import BrokerSerializer
from models import Broker
# Create your views here.

class BrokerView(ListAPIView):
    serializer_class = BrokerSerializer
    queryset = Broker.objects.all()

