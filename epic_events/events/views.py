from django.shortcuts import render
from rest_framework import viewsets, permissions

from .models import Event
from .serializers import EventSerializer
from .permissions import EventPermission, ActualDjangoModelPermissions

# Create your views here.

class EventViewset(viewsets.ModelViewSet):

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_class = [EventPermission & ActualDjangoModelPermissions]
    filterset_fields = ['event_date', 'accomplish', 'client', 'attendees']

    def get_queryset(self):
        return Event.objects.all()