from django.db import models
from products.models import Category, ProductGroup, ProductTemplate, ProductVariant

# Модель для направления услуг
class Service(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название направления")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")

    def __str__(self):
        return self.name

# Модель для типов услуг
class ServiceType(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="service_types", verbose_name="Направление")
    name = models.CharField(max_length=100, unique=True, verbose_name="Название услуги")
    description = models.TextField(blank=True, null=True, verbose_name="Описание услуги")

    def __str__(self):
        return f"{self.name} ({self.service.name})"

# Тут ошибка эта модель кажется не должна существовать
# Связь услуги с продуктами (например, услуга по конкретному товару)
class ServiceProduct(models.Model):
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE, related_name="service_products", verbose_name="Тип услуги")
    product_variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, related_name="related_services", verbose_name="Вариант товара")

    def __str__(self):
        return f"{self.service_type.name} - {self.product_variant.name}"
