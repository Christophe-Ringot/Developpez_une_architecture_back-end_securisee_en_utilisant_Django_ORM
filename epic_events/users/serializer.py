from rest_framework import serializers
from django.contrib.auth.models import Group
from .models import User


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['name',]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'password', 'email', 'is_staff']
