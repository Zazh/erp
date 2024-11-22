from django.contrib import admin
from .models import Order, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'created_at', 'status')
    list_filter = ('status', 'created_at')
    search_fields = ('client__name',)


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'get_price_list_object', 'quantity', 'total_price', 'specification_id')
    list_filter = ('order', 'price_list__content_type')
    search_fields = ('price_list__content_object__name', 'order__client__name')
    readonly_fields = ('total_price',)  # total_price только для чтения

    def save_model(self, request, obj, form, change):
        """
        Автоматический пересчет итоговой стоимости при сохранении.
        """
        obj.calculate_total_price()
        super().save_model(request, obj, form, change)

    def get_price_list_object(self, obj):
        """
        Возвращает связанный объект из прайс-листа (товар или услугу).
        """
        return obj.price_list.content_object if obj.price_list else "Нет данных"

    get_price_list_object.short_description = "Объект из прайс-листа"
