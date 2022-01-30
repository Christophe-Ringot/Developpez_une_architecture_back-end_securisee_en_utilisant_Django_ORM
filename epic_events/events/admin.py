from django.contrib import admin
from .models import Event


@admin.register(Event)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('customer', 'event_date', 'status',)
    list_filter = ('status',)
    search_fields = ('contract',)