from django.db import models
from products.models import ProductVariant
from services.models import ServiceType

# Модель типа продукта
class ProductType(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Тип продукта")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип продукта"
        verbose_name_plural = "Типы продуктов"


# Абстрактная базовая модель спецификации
class BaseSpecification(models.Model):
    service_type = models.ForeignKey(
        ServiceType,
        on_delete=models.CASCADE,
        db_index=True,
        verbose_name="Тип услуги"
    )
    product_type = models.ForeignKey(
        ProductType,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_index=True,
        verbose_name="Тип продукта"
    )
    product_variant = models.ForeignKey(
        ProductVariant,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        db_index=True,
        verbose_name="Вариант товара"
    )

    class Meta:
        abstract = True
        unique_together = ('service_type', 'product_type', 'product_variant')

    def __str__(self):
        product_name = getattr(self.product_variant, 'name', 'Нет товара')
        product_type_name = getattr(self.product_type, 'name', 'Нет типа продукта')
        return f"{self.service_type} — {product_type_name} — {product_name}"


# Спецификация для распила
class CuttingSpecification(BaseSpecification):
    cutting_file = models.FileField(
        upload_to='cutting_files/%Y/%m/%d/',
        blank=True,
        null=True,
        verbose_name="Файл кроя"
    )

    def __str__(self):
        return f"Распил: {self.service_type} — {self.product_type}"


# Спецификация для закатки
class EdgingSpecification(BaseSpecification):
    edge_thickness = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="Толщина кромки"
    )

    def __str__(self):
        return f"Закатка: {self.service_type} — {self.product_type} — {self.product_variant} (Толщина кромки: {self.edge_thickness} мм)"


# Спецификация для фасадов
class FacadeSpecification(BaseSpecification):
    coating = models.CharField(max_length=100, verbose_name="Покрытие")
    design = models.CharField(max_length=100, verbose_name="Дизайн")
    color = models.CharField(max_length=50, verbose_name="Цвет")

    def __str__(self):
        return f"Фасад: {self.service_type} — {self.product_type} — {self.product_variant} (Покрытие: {self.coating}, Дизайн: {self.design}, Цвет: {self.color})"
