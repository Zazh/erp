from django.contrib import admin
from .models import Category, ProductGroup, ProductTemplate, ProductVariant

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(ProductGroup)
class ProductGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    search_fields = ('name', 'category__name')
    list_filter = ('category',)

@admin.register(ProductTemplate)
class ProductTemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'product_group')
    search_fields = ('name', 'product_group__name')
    list_filter = ('product_group',)

@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ('name', 'product_template')
    search_fields = ('name', 'product_template__name')
    list_filter = ('product_template',)
