from django.db import models
from clients.models import Client
from pricelist.models import PriceListProduct  # Актуализированный импорт

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="orders", verbose_name="Клиент")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    status = models.CharField(max_length=50, default="Новый", verbose_name="Статус заказа")

    def __str__(self):
        return f"Заказ {self.id} для клиента {self.client}"


# Order, ProductVariant > товар, PriceList> конкретный прайс лист, quantity

class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="order_items",
        verbose_name="Заказ"
    )
    price_list = models.ForeignKey(
        PriceListProduct,
        on_delete=models.CASCADE,
        verbose_name="Товар",
        null=True,
        blank=True
    )
    quantity = models.PositiveIntegerField(
        default=1,
        verbose_name="Количество"
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        editable=False,
    )
    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        editable=False,
        verbose_name="Итоговая стоимость"
    )

    def calculate_total_price(self):
        if self.price_list:
            self.total_price = self.price_list.price_default * self.quantity
        return self.total_price

    def save(self, *args, **kwargs):
        self.calculate_total_price()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Позиция заказа {self.id} — {self.price_list.product_variant.name}"
