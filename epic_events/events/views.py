from django.shortcuts import render
from rest_framework import viewsets, permissions

from .models import Event
from .serializers import EventSerializer

# Create your views here.

class EventViewset(viewsets.ModelViewSet):

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filterset_fields = '__ALL__'