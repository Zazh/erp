from django.db import models
from itertools import product  # Для декартова произведения

# Категория товара
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Категория")

    def __str__(self):
        return self.name


# Группа товаров
class ProductGroup(models.Model):
    name = models.CharField(max_length=100, verbose_name="Группа товаров")
    category = models.ForeignKey(
        "products.Category",
        on_delete=models.CASCADE,
        related_name="product_groups",
        verbose_name="Категория"
    )

    def __str__(self):
        return f"{self.name} ({self.category.name})"


# Шаблон товара (Product Template)
class ProductTemplate(models.Model):
    name = models.CharField(max_length=100, verbose_name="Шаблон товара")
    product_group = models.ForeignKey(
        "products.ProductGroup",
        on_delete=models.CASCADE,
        related_name="product_templates",
        verbose_name="Группа товаров"
    )
    specifications = models.ManyToManyField(
        "specifications.Specification",  # Строковая ссылка на модель Specification
        related_name="templates",
        verbose_name="Спецификации",
        blank=True
    )

    def generate_variants(self):
        """
        Генерирует ProductVariant для всех возможных комбинаций спецификаций текущего шаблона.
        """
        if not self.specifications.exists():
            return 0

        from .models import ProductVariant  # Импорт внутри метода, чтобы избежать циклического импорта

        # Группируем спецификации по их типам
        specs_by_type = {}
        for spec in self.specifications.all():
            specs_by_type.setdefault(spec.specification_type, []).append(spec)

        # Создаем декартово произведение всех спецификаций
        spec_combinations = list(product(*specs_by_type.values()))

        # Генерируем варианты товаров
        created_variants = 0
        for combination in spec_combinations:
            variant_name = f"{self.name} - " + ", ".join([spec.name for spec in combination])

            # Создаем или получаем ProductVariant
            variant, created = ProductVariant.objects.get_or_create(
                name=variant_name,
                product_template=self,
                category=self.product_group.category
            )
            if created:
                # Привязываем только свои спецификации к варианту
                variant.specifications.set(combination)
                created_variants += 1

        return created_variants

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Шаблон товара"
        verbose_name_plural = "Шаблоны товаров"


# Вариант товара (Product Variant)
class ProductVariant(models.Model):
    name = models.CharField(max_length=150, verbose_name="Вариант товара")
    category = models.ForeignKey(
        "products.Category",
        on_delete=models.CASCADE,
        verbose_name="Категория"
    )
    product_template = models.ForeignKey(
        "products.ProductTemplate",
        on_delete=models.CASCADE,
        related_name="product_variants",
        verbose_name="Шаблон товара"
    )
    specifications = models.ManyToManyField(
        "specifications.Specification",
        related_name="variants",
        verbose_name="Спецификации",
        blank=True
    )

    def __str__(self):
        return self.name

    def get_price_for_client_type(self, client_type):
        """
        Возвращает цену для указанного типа клиента.
        """
        try:
            price = self.prices.get(client_type=client_type)
            return price.price
        except ProductVariantPrice.DoesNotExist:
            return None


class ProductVariantPrice(models.Model):
    product_variant = models.ForeignKey(
        "products.ProductVariant",
        on_delete=models.CASCADE,
        related_name="prices",
        verbose_name="Вариант товара"
    )
    client_type = models.ForeignKey(
        "clients.ClientType",
        on_delete=models.CASCADE,
        verbose_name="Тип клиента"
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")

    class Meta:
        unique_together = ('product_variant', 'client_type')
        verbose_name = "Цена для варианта товара"
        verbose_name_plural = "Цены для вариантов товара"

    def __str__(self):
        return f"{self.product_variant.name} - {self.client_type.name}: {self.price}"
