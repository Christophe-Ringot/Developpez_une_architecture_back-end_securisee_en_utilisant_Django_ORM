from rest_framework import serializers

from .models import Contract


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = "__all__"
        read_only_fields = ['sales_contact']

    def create(self, validated_data):
        info = Contract.objects.create(**validated_data)
        info.sales_contract = self.context["request"].user
        info.save()
        return info