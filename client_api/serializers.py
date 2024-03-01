from rest_framework import serializers

from client_api.models import ClientEntity, Request


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientEntity
        fields = '__all__'


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ['id', 'client', 'body', 'processed_by', 'status']
        read_only_fields = ['id', 'processed_by', 'status']

    def create(self, validated_data):
        validated_data['status'] = Request.PENDING
        return super().create(validated_data)
