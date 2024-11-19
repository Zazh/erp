from django.contrib import admin
from .models import (
    CuttingSpecification,
    EdgingSpecification,
    FacadeSpecification,
    ProductType
)

# Админка для модели ProductType
@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

# Базовый класс админки для ServiceSpecification
class ServiceSpecificationAdmin(admin.ModelAdmin):
    @admin.display(description='Тип услуги')
    def display_service_type(self, obj):
        return obj.service_type.name if obj.service_type else "Нет услуги"

    @admin.display(description='Тип продукта')
    def display_product_type(self, obj):
        return obj.product_type.name if obj.product_type else "Нет типа продукта"

    @admin.display(description='Вариант товара')
    def display_product_variant(self, obj):
        return obj.product_variant.name if obj.product_variant else "Нет варианта товара"

    list_display = ('display_service_type', 'display_product_type', 'display_product_variant')
    list_filter = ('service_type', 'product_type', 'product_variant')
    search_fields = ('service_type__name', 'product_type__name', 'product_variant__name')

# Админка для CuttingSpecification
@admin.register(CuttingSpecification)
class CuttingSpecificationAdmin(ServiceSpecificationAdmin):
    @admin.display(description='Файл кроя')
    def display_cutting_file(self, obj):
        return obj.cutting_file

    list_display = ('display_service_type', 'display_product_type', 'display_product_variant', 'display_cutting_file')
    list_filter = ('service_type', 'product_type', 'product_variant')
    search_fields = ('service_type__name', 'product_type__name', 'product_variant__name')

# Админка для EdgingSpecification
@admin.register(EdgingSpecification)
class EdgingSpecificationAdmin(ServiceSpecificationAdmin):
    @admin.display(description='Толщина кромки')
    def display_edge_thickness(self, obj):
        return obj.edge_thickness

    list_display = ('display_service_type', 'display_product_type', 'display_product_variant', 'display_edge_thickness')
    list_filter = ('service_type', 'product_type', 'product_variant', 'edge_thickness')
    search_fields = ('service_type__name', 'product_type__name', 'product_variant__name')

# Админка для FacadeSpecification
@admin.register(FacadeSpecification)
class FacadeSpecificationAdmin(ServiceSpecificationAdmin):
    @admin.display(description='Покрытие')
    def display_coating(self, obj):
        return obj.coating

    @admin.display(description='Дизайн')
    def display_design(self, obj):
        return obj.design

    @admin.display(description='Цвет')
    def display_color(self, obj):
        return obj.color

    list_display = ('display_service_type', 'display_product_type', 'display_product_variant', 'display_coating', 'display_design', 'display_color')
    list_filter = ('service_type', 'product_type', 'product_variant', 'coating', 'design')
    search_fields = ('service_type__name', 'product_type__name', 'coating', 'design', 'product_variant__name')

# Кастомизация отображения категорий в админке
admin.site.index_title = "Specifications"
admin.site.site_title = "Service and Product Specifications"
admin.site.site_header = "Specifications Administration"
