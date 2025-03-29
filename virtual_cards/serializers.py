from rest_framework import serializers
from .models import VirtualCard

class VirtualCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = VirtualCard
        fields = ['id', 'card_number', 'expiry_date', 'cvv', 'currency', 'is_active', 'created_at']