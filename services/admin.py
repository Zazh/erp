from django.contrib import admin

from .models import (
    Service,
    ServiceType,
)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(ServiceType)
class ServiceTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'service', 'description')
    list_filter = ('service',)
    search_fields = ('name',)
