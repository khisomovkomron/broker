from rest_framework.generics import GenericAPIView, RetrieveDestroyAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from . import serializers
from broker import models

    
class SharesListCreateView(GenericAPIView):
    serializer_class = serializers.SharesSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get_queryset(self):
        shares = models.Shares.objects.all()
        return shares
    
    def get(self, requests, *args, **kwargs):
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
    

class SharesRetrieveView(GenericAPIView):
    serializer_class = serializers.SharesSerializer
    permission_classes = [IsAuthenticated]


    def get(self, request, *args, **kwargs):

        id = request.query_params.get('id')
        share = models.Shares.objects.get(id=id)
        serializer = serializers.SharesSerializer(share)
        
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        id = request.query_params['id']
        share_object = models.Shares.objects.get(id=id)
        data = request.data
    
        share_object.title = data.get('title', share_object.title)
        share_object.description = data.get('description', share_object.description)
        share_object.total_shares = data.get('total_shares', share_object.total_shares)
        share_object.price = data.get('price', share_object.price)
    
        share_object.save()
        serializer = serializers.SharesSerializer(share_object)
    
        return Response(serializer.data)

class SharesUpdateView(GenericAPIView):
    serializer_class = serializers.SharesSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        id = request.query_params['id']
        share = models.Shares.objects.get(id=id)
        serializer = serializers.SharesSerializer(share)
    
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        id = request.query_params['id']
        share_object = models.Shares.objects.get(id=id)
    
        data = request.data
    
        share_object.title = data['title']
        share_object.description = data['description']
        share_object.total_shares = data['total_shares']
        share_object.price = data['price']
    
        serializer = serializers.SharesSerializer(share_object)
        return Response(serializer.data)
        

class SharesDetailView(RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.SharesSerializer
    queryset = models.Shares.objects.all()