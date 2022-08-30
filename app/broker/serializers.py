from models import Broker
from rest_framework import serializers


class BrokerSerializer(serializers.ModelSerializer):

    class meta:
        model = Broker
        fields = ['id', 'title', 'description']