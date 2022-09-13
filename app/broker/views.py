from django.shortcuts import render
from rest_framework import generics, viewsets, mixins
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
    queryset = models.Broker.objects.all()
    
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
    
class BrokerViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.BrokerSerializer
    permission_classes = [IsAuthenticated]
    queryset = models.Broker.objects.all()
    
    def _params_to_ints(self, qs):
        print(qs)
        return [int(str_id) for str_id in qs.split(',')]
    
    def get_queryset(self):
        shares = self.request.query_params.get('shares')
        queryset = self.queryset
        if shares:
            share_ids = self._params_to_ints(shares)
            print(share_ids)
            queryset = queryset.filter(shares__id__in=share_ids)
            print(queryset)
            
        return queryset.filter(user=self.request.user).order_by('-id').distinct()
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
class BaseBrokerAttrViewset(mixins.DestroyModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.ListModelMixin,
                            viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        
        assigned_only = bool(
            int(self.request.query_params.get('assigned_only', 0))
        )
        queryset = self.queryset
        if assigned_only:
            queryset = queryset.filter(broker__isnull=False)
            
        return queryset.filter(user=self.request.user).order_by('-name').distinct()
    
class SharesViewSet(BaseBrokerAttrViewset):
    serializer_class = serializers.SharesSerializer
    queryset = models.Shares.objects.all()
    
    
