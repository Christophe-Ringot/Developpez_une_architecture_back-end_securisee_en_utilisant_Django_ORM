from rest_framework import serializers

from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"
        read_only_fields = ['sales_contract']

    def create(self, validated_data):
        info = Customer.objects.create(**validated_data)
        info.sales_contract = self.context["request"].user
        info.save()
        return info