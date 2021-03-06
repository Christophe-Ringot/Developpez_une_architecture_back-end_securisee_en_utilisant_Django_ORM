from django.db import models
from django.conf import settings


class Customer(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='First name')
    last_name = models.CharField(max_length=30, verbose_name='Last name')
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    status = models.TextField(default="prospect", choices=(("prospect", "prospect"),("acquired", "acquired")))
    company_name = models.CharField(max_length=250)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    sales_contact = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                       on_delete=models.CASCADE, blank=True,
                                       null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
