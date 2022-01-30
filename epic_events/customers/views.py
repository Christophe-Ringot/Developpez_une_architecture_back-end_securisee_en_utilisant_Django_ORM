from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Customer
from .serializer import CustomerSerializer
from .permissions import CustomerPermission


class CustomerViewSet(viewsets.ModelViewSet):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [CustomerPermission]
    filterset_fields = ['first_name', 'company_name']
    search_fields = ['first_name', 'last_name']

    @action(detail=False, methods=['GET'])
    def my_customers(self, request, **kwargs):
        queryset = self.get_queryset().filter(sales_contact=self.request.user)
        serializer = CustomerSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)