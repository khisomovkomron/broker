from .models import (
    Broker,
    User,
    Shares
)
from rest_framework import serializers
from shares.serializers import SharesSerializer


class BrokerSerializer(serializers.ModelSerializer):
    shares = SharesSerializer(many=True)

    class Meta:
        model = Broker
        fields = ['id', 'title', 'description', 'shares']
            
    def create(self, validated_data):
        shares = validated_data.pop('shares')
        broker = Broker.objects.create(**validated_data)
        for share in shares:
            shares_obj, created = Shares.objects.get_or_create(broker=broker, **share)
            broker.shares.add(shares_obj)
        
        return broker
    
    # def update(self, instance, validated_data):
    #     shares = validated_data.pop('shares', None)
    #     if shares is not None:
    #         instance.shares.clear()
    #         self._get_or_create_shares(shares, instance)
    #
    #     for attr, value in validated_data.items():
    #         setattr(instance, attr, value)
    #
    #     instance.save()
    #     return instance
    

class BrokerApiViewSerialiazer(serializers.ModelSerializer):
    
    class Meta:
        model = Broker
        fields = ('title', 'description',)
        
        
        