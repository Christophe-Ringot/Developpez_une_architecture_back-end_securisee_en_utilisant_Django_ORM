from django.db import models
from django.conf import settings
from customers.models import Customer
from django.utils import timezone
import datetime


class Contract(models.Model):

    sales_contact = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        blank=True, null=True)
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

    def __str__(self):
        return f"{self.customer}'s contract"
