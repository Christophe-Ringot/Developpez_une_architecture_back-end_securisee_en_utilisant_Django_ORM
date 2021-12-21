from django.db import models


# Create your models here.
class Customers(models.Model):
    first_name = models.Charfield(max_length=30, verbose_name='First name')
    last_name = models.Charfield(max_length=30, verbose_name='Last name')
    email = models.EmailField(max_length=100)
    phone = models.Charfield(max_length=20)
    mobile = models.Charfield(max_length=20)
    company_name = models.Charfield(max_length=250)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    sales_contract = models.ForeignKey(on_delete=models.CASCADE)
