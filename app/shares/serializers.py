from broker import models
from rest_framework import serializers


class SharesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Shares
        fields = '__all__'