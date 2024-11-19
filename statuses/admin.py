from django.contrib import admin
from .models import StatusCategory, Status

@admin.register(StatusCategory)
class StatusCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'is_active', 'color')
    list_filter = ('category', 'is_active')
    search_fields = ('name', 'category__name')
