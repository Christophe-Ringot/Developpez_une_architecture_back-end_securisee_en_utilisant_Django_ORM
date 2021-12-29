from django.shortcuts import render
from rest_framework import viewsets, permissions

from .models import Customer
from .serializer import CustomerSerializer

# Create your views here.

class CustomerViewset(viewsets.ModelViewset):

    queryset = Customer.object.all()
    serialize_class = CustomerSerializer
    permission_classes = [CustomerPermission | permissions.IsAdminUser]
    filterset_fields = ['first_name', 'company_name']