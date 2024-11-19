from django.contrib import admin
from .models import PriceListProduct, PriceListService

@admin.register(PriceListProduct)
class PriceListProductAdmin(admin.ModelAdmin):
    list_display = (
        'product_variant',
        'price_default',
        'price_individual',
        'price_business',
    )
    list_filter = ('product_variant',)
    search_fields = ('product_variant__name',)

    fieldsets = (
        (None, {
            'fields': ('product_variant',)
        }),
        ('Цены для типов клиентов', {
            'fields': ('price_individual', 'price_business', 'price_default')
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['product_variant']
        return []

@admin.register(PriceListService)
class PriceListServiceAdmin(admin.ModelAdmin):
    list_display = (
        'service_type',
        'category',
        'product_group',
        'price_default',
        'price_individual',
        'price_business',
    )
    list_filter = ('service_type', 'category', 'product_group')
    search_fields = ('service_type__name', 'product_group__name', 'category__name')

    fields = ('service_type', 'category', 'product_group', 'price_individual', 'price_business', 'price_default')

    def get_readonly_fields(self, request, obj=None):
        # Убираем поля `category` и `product_group` из "только для чтения"
        if obj:
            return ['service_type']
        return []
