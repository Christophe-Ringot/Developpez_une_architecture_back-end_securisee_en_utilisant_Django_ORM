from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import Group

from .models import User
from .serializer import UserSerializer, GroupSerializer
from .permissions import UserPermission, GroupPermission, ActualDjangoModelPermissions

class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserPermission, ActualDjangoModelPermissions]

    @action(detail=False, methods=['GET'])
    def my_own_user(self, request, **kwargs):
        queryset = self.get_queryset().filter(username=self.request.user)
        serializer = UserSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)


class GroupViewSet(viewsets.ModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [GroupPermission]
