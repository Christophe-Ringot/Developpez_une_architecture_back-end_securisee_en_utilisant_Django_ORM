from django.shortcuts import render
from rest_framework import viewsets, permissions

from .models import Contract
from .serializer import ContractSerializer
from .permissions import ContractPermission

# Create your views here.

class ContractViewset(viewsets.ModelViewSet):

    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [(ContractPermission & permissions.IsAuthenticated)]

    def get_queryset(self, *args, **kwargs):
        queryset = self.get_queryset().filter\
            (support_contact=self.request.user)
        serializer = ContractSerializer(queryset,
                                     many=True, context={'request': request})
        return Response(serializer.data)
