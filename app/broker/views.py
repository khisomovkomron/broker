from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

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


class BrokerNestedView(generics.GenericAPIView):
    serializer_class = serializers.BrokerApiViewSerialiazer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        brokers = models.Broker.objects.all()
        return brokers
    
    def get(self, request, *args, **kwargs):
        try:
            id = request.query_params['id']
            print(id)
            broker = models.Broker.objects.get(title=id)
            print(broker)
            serializer = serializers.BrokerApiViewSerialiazer(broker)
        except:
            broker = self.get_queryset()
            print(broker)
            serializer = serializers.BrokerApiViewSerialiazer(broker, many=True)

        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        broker = request.data
        # id = request.data['shares']['id']
        # print(id)
        new_broker = models.Broker.objects.create(title=broker['title'], description=broker['description'])
        new_broker.save()
        
        serializer = serializers.BrokerApiViewSerialiazer(new_broker)
        
        return Response(serializer.data)
