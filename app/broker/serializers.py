from . import models
from rest_framework import serializers


class BrokerSerializer(serializers.ModelSerializer):

    class meta:
        model = models.Broker
        fields = ['id', 'title', 'description']