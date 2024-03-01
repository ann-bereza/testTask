from rest_framework import serializers

from client_api.models import Request
from operator_api.models import Operator


class OperatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operator
        fields = '__all__'


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ['id', 'client', 'body', 'processed_by', 'status']
        read_only_fields = ['id', 'body', 'client']
