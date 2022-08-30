from rest_framework import serializers
from .models import Broker


class BrokeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Broker
        fields = ['id', 'title', 'description']
        
    