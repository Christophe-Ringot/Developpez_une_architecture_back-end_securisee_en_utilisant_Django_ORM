from django.db import models
from customers.models import Customer
from users.models import User
from django.utils import timezone


class Event(models.Model):

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,
                               related_name='events')
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(default=timezone.now)
    support_contact = models.ForeignKey(User,on_delete=models.CASCADE, blank=True, null=True)
    status = models.TextField(choices=(("on_going", "On going"), ("finished", "Finished")))
    attendees = models.IntegerField(default=0)
    event_date = models.DateTimeField(default=timezone.now)
    notes = models.TextField(max_length=2500, blank=True)
