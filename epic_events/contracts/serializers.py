from rest_framework import serializers

from .models import Contract


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = "__all__"
        read_only_fields = ['sales_contact']

    def create(self, validated_data):
        info = Contract.objects.create(**validated_data)
        info.sales_contact = self.context["request"].user
        Event.objects.create(event_contract=info, client=info.client)
        client = Client.objects.get(id=info.client_id)
        client.converted = True
        client.save()
        info.save()
        return info