from django.shortcuts import render
from rest_framework import viewsets

from .models import Contract
from .serializer import ContractSerializer

# Create your views here.

class ContractViewset(viewsets.ModelViewSet):

    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
