from rest_framework import serializers
from django.contrib.auth.models import User
from core.models import Profile


class UserSerializer(serializers.ModelSerializer):
    profile = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profile']