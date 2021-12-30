from django.shortcuts import render
from rest_framework import viewsets, permissions

from .models import Customer
from .serializer import CustomerSerializer
from .permissions import CustomerPermission

# Create your views here.

class CustomerViewset(viewsets.ModelViewSet):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_class = [CustomerPermission & permissions.IsAuthenticated]
    filterset_fields = ['first_name', 'company_name']
    search_fields = ['first_name', 'last_name']