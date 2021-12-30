from rest_framework import serializers

from .models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"
        read_only_fields = ['sales_contact']

    def create(self, validated_data):
        info = Event.objects.create(**validated_data)
        info.sales_contact = self.context["request"].user
        info.save()
        return info