from django.db import models
from django.contrib.auth.models import User
from customers.models import Customer
from django.utils import timezone
import datetime


# Create your models here.
class Contract(models.Model):
    sales_contract = models.ForeignKey(User, on_delete=models.CASCADE,
                                       null=False, blank=False)
    client =  models.ForeignKey(Customer, on_delete=models.CASCADE,
                                null=False, blank=False)
    date_created = models.DateTimeField(default=timezone.now,
                                        null=False, blank=False)
    date_updated = models.DateTimeField(default=timezone.now,
                                        null=False, blank=False)
    status = models.BooleanField(default=None)
    amount = models.FloatField(null=False, blank=False)
    payment_due = models.DateTimeField(null=False, blank=False)