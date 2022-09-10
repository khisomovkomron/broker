from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from . import serializers
from broker import models


class SharesListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = serializers.SharesSerializer
    queryset = models.Shares.objects.all()
    
    
class SharesDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.SharesSerializer
    queryset = models.Shares.objects.all()
    
    
class SharesGetView(generics.GenericAPIView):
    serializer_class = serializers.SharesSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        shares = models.Shares.objects.all()
        return shares
    
    def get(self, request, *args, **kwargs):
        try:
            id = request.query_params['id']
            share = models.Shares.objects.get(id=id)
            serializer = serializers.SharesSerializer(share)
        except:
            share = self.get_queryset()
            serializer = serializers.SharesSerializer(share, many=True)
        
        return Response(serializer.data)
        
    def post(self, request, *args, **kwargs):
        share = request.data
        
        new_share = models.Shares.objects.create(title=share['title'],
                                                 description=share['description'],
                                                 total_shares=share['total_shares'],
                                                 price=share['price'])
        new_share.save()
        
        serializer = serializers.SharesSerializer(new_share)
        
        return Response(serializer.data)
    
