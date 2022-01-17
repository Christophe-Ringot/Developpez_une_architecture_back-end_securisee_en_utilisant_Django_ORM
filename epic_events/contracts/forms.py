from .models import Contract
from ..customers.models import Customer
from django.forms import ModelForm
from django.contrib.auth.models import User

class ContractForm(ModelForm):
    class Meta:
        model = Contract
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sales_contact' in self.fields:
            self.fields['sales_contact'].queryset = User.objects.filter\
                (groups__name='Sales')
            self.fields['customer'].queryset = Customer.objects.filter\
                (status='acquired')