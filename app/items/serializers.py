from . import models
from rest_framework import serializers


class ItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Items
        fields = '__all__'