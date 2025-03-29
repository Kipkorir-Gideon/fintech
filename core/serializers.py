from rest_framework import serializers
from .models import Profile, Transaction

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['phone_number', 'kyc_verified', 'currency']
        

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'amount', 'currency', 'transaction_type', 'status', 'created_at', 'updated_at']