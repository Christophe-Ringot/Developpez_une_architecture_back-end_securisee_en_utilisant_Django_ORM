from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Event
from .serializers import EventSerializer
from .permissions import EventPermission


class EventViewSet(viewsets.ModelViewSet):

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [EventPermission]
    filterset_fields = ['event_date', 'accomplish', 'client', 'attendees']

    @action(detail=False, methods=['GET'])
    def my_events(self, request, **kwargs):
        queryset = self.get_queryset().filter(support_contact=self.request.user)
        serializer = EventSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)