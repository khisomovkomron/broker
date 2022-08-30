from . import models
from rest_framework import serializers


class BrokerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Broker
        fields = ['id', 'title', 'description']