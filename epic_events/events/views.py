from django.shortcuts import render
from rest_framework import viewsets, permissions

from .models import Event
from .serializers import EventSerializer
from .permissions import EventPermission

# Create your views here.

class EventViewset(viewsets.ModelViewSet):

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_class = [EventPermission & permissions.IsAuthenticated]
    filterset_fields = ['event_date', 'accomplish', 'client', 'attendees']

    def get_queryset(self, *args, **kwargs):
        queryset = self.get_queryset().filter\
            (support_contact=self.request.user)
        serializer = EventSerializer(queryset,
                                     many=True, context={'request': request})
        return Response(serializer.data)