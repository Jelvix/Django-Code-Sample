from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'date_added', 'is_active', 'avatar', 'is_staff', 'password')

    def validate_password(self, value):
        return make_password(value)


class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'date_added', 'is_active', 'avatar', 'is_staff')
