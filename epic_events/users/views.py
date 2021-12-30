from rest_framework import viewsets, permissions
from django.contrib.auth.models import User, Group
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializer import UserSerializer, GroupSerializer
from .permissions import UserPermission, GroupPermission


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [(UserPermission & permissions.IsAuthenticated)]

    @action(detail=False, methods=['GET'])
    def my_own_user(self, request, **kwargs):
        queryset = self.get_queryset().filter(username=self.request.user)
        serializer = UserSerializer(queryset, many=True, context=
        {'request': request})
        return Response(serializer.data)


class GroupViewSet(viewsets.ModelViewSet):

    queryset = Group.objects.all().order_by('id')
    serializer_class = GroupSerializer
    permission_classes = [(GroupPermission & permissions.IsAuthenticated)]