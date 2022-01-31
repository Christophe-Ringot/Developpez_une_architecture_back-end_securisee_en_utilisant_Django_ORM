from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Contract
from .serializers import ContractSerializer
from .permissions import ContractPermission


class ContractViewSet(viewsets.ModelViewSet):

    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [ContractPermission]

    @action(detail=False, methods=['GET'])
    def my_contracts(self, request, **kwargs):
        queryset = self.get_queryset().filter(sales_contact=self.request.user)
        serializer = ContractSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
