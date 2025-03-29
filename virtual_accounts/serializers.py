from rest_framework import serializers
from .models import VirtualAccount


class VirtualAccountSerializer(serializers.Serializer):
    class Meta:
        model = VirtualAccount
        fields = ['id', 'account_number', 'bank_name', 'currency', 'balance', 'created_at']