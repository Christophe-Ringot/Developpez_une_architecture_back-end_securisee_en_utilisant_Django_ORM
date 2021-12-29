from django.shortcuts import render
from rest_framework import viewsets, permissions

from .models import Customer
from .serializer import CustomerSerializer

# Create your views here.

class CustomerViewset(viewsets.ModelViewSet):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filterset_fields = ['first_name', 'company_name']