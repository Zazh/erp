from django.contrib import admin
from .models import Specification, SpecificationType, TemplateSpecification, ProductVariantSpecification


@admin.register(SpecificationType)
class SpecificationTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'unit_type')  # Отображение полей в списке
    search_fields = ('name',)  # Поле для поиска
    ordering = ('name',)  # Сортировка по умолчанию


@admin.register(Specification)
class SpecificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'specification_type', 'product_variant')  # Отображаемые поля
    search_fields = ('name', 'value', 'specification_type__name')  # Поля для поиска
    list_filter = ('specification_type', 'product_variant')  # Боковые фильтры
    ordering = ('name',)  # Сортировка по умолчанию
    autocomplete_fields = ('specification_type', 'product_variant')  # Для быстрого поиска связанных объектов
    fieldsets = (
        (None, {
            'fields': ('name', 'value', 'specification_type', 'product_variant'),
        }),
    )


@admin.register(TemplateSpecification)
class TemplateSpecificationAdmin(admin.ModelAdmin):
    list_display = ('product_template', 'specifications_id')  # Отображаемые поля
    search_fields = ('product_template__name', 'specifications_id__name')  # Поля для поиска
    list_filter = ('product_template', 'specifications_id')  # Фильтры
    autocomplete_fields = ('product_template', 'specifications_id')  # Ускорение выбора связанных объектов
    ordering = ('product_template',)  # Сортировка по умолчанию
    fieldsets = (
        (None, {
            'fields': ('product_template', 'specifications_id'),
        }),
    )


@admin.register(ProductVariantSpecification)
class ProductVariantSpecificationAdmin(admin.ModelAdmin):
    list_display = ('product_variant', 'specifications_id')  # Отображаемые поля
    search_fields = ('product_variant__name', 'specifications_id__name')  # Поля для поиска
    list_filter = ('product_variant', 'specifications_id')  # Фильтры
    autocomplete_fields = ('product_variant', 'specifications_id')  # Ускорение выбора связанных объектов
    ordering = ('product_variant',)  # Сортировка по умолчанию
    fieldsets = (
        (None, {
            'fields': ('product_variant', 'specifications_id'),
        }),
    )
