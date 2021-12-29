from django.contrib import admin
from .models import Contract
from django.contrib import admin


# Register your models here.

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    search_fields = ('client',)