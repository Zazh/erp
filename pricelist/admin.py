from django.contrib import admin
from .models import PriceList
from django.contrib.contenttypes.admin import GenericTabularInline


@admin.register(PriceList)
class PriceListAdmin(admin.ModelAdmin):
    list_display = (
        'content_object',  # Показывает связанный объект (товар или услугу)
        'get_content_type',  # Показывает тип объекта (товар или услуга)
        'price_default',
        'price_individual',
        'price_business',
    )
    list_filter = ('content_type',)  # Фильтр по типу объекта (товар или услуга)
    search_fields = ('content_type__model', 'object_id')  # Поиск по типу объекта и ID объекта

    fieldsets = (
        (None, {
            'fields': ('content_type', 'object_id', 'content_object')
        }),
        ('Цены для типов клиентов', {
            'fields': ('price_individual', 'price_business', 'price_default')
        }),
    )

    readonly_fields = ('content_object',)

    def get_readonly_fields(self, request, obj=None):
        # Делаем `content_type` и `object_id` readonly, если запись уже существует
        if obj:
            return ['content_type', 'object_id'] + self.readonly_fields
        return self.readonly_fields

    def get_content_type(self, obj):
        """
        Возвращает человекочитаемый тип связанного объекта (товар или услуга).
        """
        return obj.content_type.name.capitalize() if obj.content_type else "Неизвестно"

    get_content_type.short_description = "Тип объекта"
