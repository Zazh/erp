# admin.py
from django.contrib import admin
from .models import Order, OrderItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'created_at', 'status')
    list_filter = ('status', 'created_at')
    search_fields = ('client__name',)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'price_list', 'quantity', 'total_price')
    list_filter = ('order', 'price_list')
    search_fields = ('price_list__product__name', 'order__client__name')
    readonly_fields = ('total_price',)  # total_price только для чтения

    def save_model(self, request, obj, form, change):
        if obj.price_list:
            obj.calculate_total_price()
        super().save_model(request, obj, form, change)
