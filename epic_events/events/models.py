from django.db import models
from ..customers.models import Customers
from ..contracts.models import Contracts
from django.contrib.auth.models import User
from django.utils import timezone, dateformat

# Create your models here.
class Events(models.Model):
    client = models.ForeignKey(Customers, on_delete=models.CASCADE,
                               related_name='events')
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(default=timezone.now)
    support_contract = models.ForeignKey(User, on_delete=models.CASCADE)
    event_status = models.ForeignKey(choice=EVENT_STATUS)
    attendees = models.IntegerField(default=0)
    event_date = models.DateTimeField(default=timezone.now)
    notes = models.TextField(max_length=2000, blank=True)
    contract=models.OneToOneField(Contracts, on_delete=models.CASCADE,
                                  null=True, blank=True)