from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from . import serializers
from . import models


class ItemListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = serializers.ItemSerializer
    queryset = models.Items.objects.order_by('title').values()
    
    
class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.ItemSerializer
    queryset = models.Items.objects.all()
