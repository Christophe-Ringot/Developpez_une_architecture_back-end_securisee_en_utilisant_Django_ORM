from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializer import UserSerializer
from .permissions import ActualDjangoModelPermissions
from rest_framework.permissions import DjangoModelPermissions



# Create your views here.

class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [ActualDjangoModelPermissions]
