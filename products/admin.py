# products/admin.py

from django.contrib import admin
from .models import Category, ProductGroup, ProductTemplate, ProductVariant, ProductVariantPrice

# Убираем ClientType, потому что он относится к clients/admin.py

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
    filter_horizontal = ('specifications',)
    fieldsets = (
        (None, {
            'fields': ('name', 'product_group', 'specifications'),
        }),
    )

    actions = ['generate_variants']

    @admin.action(description="Сгенерировать все возможные варианты товара")
    def generate_variants(self, request, queryset):
        total_created = 0
        for template in queryset:
            created_count = template.generate_variants()
            total_created += created_count

        self.message_user(request, f"Создано {total_created} вариантов товара.")


class ProductVariantPriceInline(admin.TabularInline):
    model = ProductVariantPrice
    extra = 1
    min_num = 1
    max_num = 10
    fields = ('client_type', 'price')
    autocomplete_fields = ['client_type']


@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ('name', 'product_template', 'category', 'display_specifications')
    search_fields = ('name', 'product_template__name', 'category__name')
    list_filter = ('product_template', 'category')
    readonly_fields = ('display_specifications',)
    exclude = ('specifications',)
    inlines = [ProductVariantPriceInline]

    def display_specifications(self, obj):
        return ", ".join([spec.name for spec in obj.specifications.all()])

    display_specifications.short_description = "Спецификации"


@admin.register(ProductVariantPrice)
class ProductVariantPriceAdmin(admin.ModelAdmin):
    list_display = ('product_variant', 'client_type', 'price')
    search_fields = ('product_variant__name', 'client_type__name')
    list_filter = ('client_type',)
    autocomplete_fields = ['product_variant', 'client_type']
