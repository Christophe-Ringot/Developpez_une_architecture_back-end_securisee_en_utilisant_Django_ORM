from rest_framework import serializers

from .models import Contract
from customers.models import Customer


class ContractSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contract
        fields = "__all__"
        read_only_fields = ['sales_contact']

    def create(self, validated_data):
        info = Contract.objects.create(**validated_data)
        info.sales_contact = self.context["request"].user
        customer = Customer.objects.get(id=info.customer_id)
        customer.converted = True
        customer.save()
        info.save()
        return info