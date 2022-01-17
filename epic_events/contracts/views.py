from django.shortcuts import render
from rest_framework import viewsets, permissions

from .models import Contract
from .serializer import ContractSerializer
from .permissions import ContractPermission, ActualDjangoModelPermissions

# Create your views here.

class ContractViewset(viewsets.ModelViewSet):

    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [(ContractPermission & ActualDjangoModelPermissions)]

    def get_queryset(self):
        return Contract.objects.all()
