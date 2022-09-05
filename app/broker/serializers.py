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
        
    # def _get_or_create_shares(self, shares, broker):
    #     auth_user = self.context['request'].user
    #     for share in shares:
    #         share_obj, created = Shares.object.get_or_create(
    #             user=auth_user,
    #             **share,
    #         )
    #         broker.shares.add(share_obj)
            
    def create(self, validated_data):
        shares = validated_data.pop('shares')
        broker = Broker.objects.create(**validated_data)
        for share in shares:
            Shares.objects.get_or_create(broker=broker, **share)
        
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
        
        
        
        