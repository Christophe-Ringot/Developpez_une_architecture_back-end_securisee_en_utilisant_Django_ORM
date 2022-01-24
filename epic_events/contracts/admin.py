from django.contrib import admin
from .models import Contract


# Register your models here.

@admin.register(Contract)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('customer', 'date_created', 'sales_contact', 'status')
    list_filter = ('status',)
