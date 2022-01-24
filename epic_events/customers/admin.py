from django.contrib import admin
from .models import Customer

# Register your models here.

@admin.register(Customer)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','company_name' ,'phone', 'status')
    list_filter = ('status',)
    search_fields = ('first_name', 'last_name', 'company_name' )