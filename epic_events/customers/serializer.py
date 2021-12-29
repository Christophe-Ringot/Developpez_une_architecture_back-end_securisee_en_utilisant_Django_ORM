from rest_framework import serializers

from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = "__all__"

    def create(self, validated_data):
        pass