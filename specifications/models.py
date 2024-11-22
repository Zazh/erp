from django.db import models

# Тип спецификации
class SpecificationType(models.Model):
    name = models.CharField(max_length=150, verbose_name="Тип спецификации")
    unit_type = models.CharField(
        max_length=150,
        verbose_name="Единица измерения",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name or "Без названия"

    class Meta:
        verbose_name = "Тип спецификации"
        verbose_name_plural = "Типы спецификаций"


# Спецификация
class Specification(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название")
    value = models.CharField(max_length=150, verbose_name="Значение")
    specification_type = models.ForeignKey(
        SpecificationType,
        on_delete=models.CASCADE,
        related_name="product_groups",
        verbose_name="Тип спецификации"
    )

    product_variant = models.ForeignKey(
        "products.ProductVariant",  # Строковый путь
        on_delete=models.CASCADE,
        verbose_name="Вариант продукта",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name or "Без названия"

    class Meta:
        verbose_name = "Спецификация"
        verbose_name_plural = "Спецификации"


# Связь спецификации и шаблона
class TemplateSpecification(models.Model):
    product_template = models.ForeignKey(
        "products.ProductTemplate",  # Строковый путь
        on_delete=models.CASCADE,
        related_name="product_templates",
        verbose_name="Шаблон продукта"
    )

    specifications_id = models.ForeignKey(
        Specification,
        on_delete=models.CASCADE,
        verbose_name="ID спецификации",
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.product_template} - {self.specifications_id}"

    class Meta:
        verbose_name = "Связь спецификации и шаблона"
        verbose_name_plural = "Связи спецификаций и шаблонов"


# Связь спецификации и варианта продукта
class ProductVariantSpecification(models.Model):
    product_variant = models.ForeignKey(
        "products.ProductVariant",  # Строковый путь
        on_delete=models.CASCADE,
        related_name="variant_specifications",
        verbose_name="Вариант продукта"
    )

    specifications_id = models.ForeignKey(
        Specification,
        on_delete=models.CASCADE,
        verbose_name="ID спецификации",
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.product_variant} - {self.specifications_id}"

    class Meta:
        verbose_name = "Связь спецификации и варианта товара"
        verbose_name_plural = "Связи спецификаций и вариантов товаров"
