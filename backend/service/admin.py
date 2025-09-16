from django.contrib import admin
from .models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    """
    Admin interface for Service model
    """
    list_display = ['name', 'type', 'paid', 'admin', 'url']
    list_filter = ['type', 'paid', 'admin']
    search_fields = ['name', 'description', 'url']
    list_editable = ['paid', 'admin']
    ordering = ['name']
