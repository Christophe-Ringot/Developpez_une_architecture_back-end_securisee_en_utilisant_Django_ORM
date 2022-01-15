from django.db import models
from django.contrib.auth.models import User
from customers.models import Customer
from django.utils import timezone
import datetime


# Create your models here.
class Contract(models.Model):

    def __str__(self):
        return f'Contract for: {self.customer}'

    sales_contract = models.ForeignKey(User, on_delete=models.CASCADE,
                                       null=False, blank=False)
    customer =  models.ForeignKey(Customer, on_delete=models.CASCADE,
                                null=False, blank=False)
    date_created = models.DateTimeField(default=timezone.now,
                                        null=False, blank=False)
    date_updated = models.DateTimeField(default=timezone.now,
                                        null=False, blank=False)
    status = models.BooleanField(default=False,
                                 verbose_name="Contract signed ?")
    amount = models.FloatField(null=False, blank=False)
    payment_due = models.DateTimeField(null=False, blank=False)