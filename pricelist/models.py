from django.db import models
from clients.models import ClientType
from services.models import ServiceType
from products.models import ProductVariant, Category, ProductGroup

# Модель для прайс-листа товаров
class PriceListProduct(models.Model):
    product_variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, verbose_name="Вариант товара", null=False)
    price_individual = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена для Individual", null=True, blank=True)
    price_business = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена для Business", null=True, blank=True)
    price_default = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена по умолчанию", null=True, blank=True)

    def __str__(self):
        return f"Прайс-лист для {self.product_variant.name}: {self.get_price_display()}"

    def get_price(self, client_type):
        """
        Возвращает цену в зависимости от типа клиента.
        """
        if client_type.name == "Individual" and self.price_individual is not None:
            return self.price_individual
        elif client_type.name == "Business" and self.price_business is not None:
            return self.price_business
        else:
            return self.price_default

    def get_price_display(self):
        """
        Возвращает строку с ценами для всех типов клиентов.
        """
        return f"Individual: {self.price_individual}, Business: {self.price_business}, Default: {self.price_default}"


# Модель для прайс-листа услуг
class PriceListService(models.Model):
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE, verbose_name="Тип услуги")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория товара")
    product_group = models.ForeignKey(ProductGroup, on_delete=models.CASCADE, verbose_name="Группа товаров")
    price_individual = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена для Individual", null=True, blank=True)
    price_business = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена для Business", null=True, blank=True)
    price_default = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена по умолчанию", null=True, blank=True)

    class Meta:
        unique_together = ('service_type', 'product_group')

    def __str__(self):
        return f"Прайс-лист для {self.service_type.name} ({self.product_group.name}): {self.get_price_display()}"

    def get_price(self, client_type):
        """
        Возвращает цену в зависимости от типа клиента.
        """
        if client_type.name == "Individual" and self.price_individual is not None:
            return self.price_individual
        elif client_type.name == "Business" and self.price_business is not None:
            return self.price_business
        else:
            return self.price_default

    def get_price_display(self):
        """
        Возвращает строку с ценами для всех типов клиентов.
        """
        return f"Individual: {self.price_individual}, Business: {self.price_business}, Default: {self.price_default}"
