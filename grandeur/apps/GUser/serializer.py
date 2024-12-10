from rest_framework import serializers

from .models import GUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = GUser
        fields = '__all__'