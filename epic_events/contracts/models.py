from django.db import models
from django.contrib.auth.models import User
from ..customers.models import Customers
from django.utils import timezone
import datetime

# Create your models here.

class Contracts(models.Model):
    sales_contract = models.ForeignKey(User, on_delete=models.CASCADE)
    client =  models.ForeignKey(Customers, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=0)
    amount = models.FloatField(default=0)
    payment_due = models.DateTimeField(default=datetime.date.today)