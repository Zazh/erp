from django.db import models
from clients.models import Client
from pricelist.models import PriceList


class Order(models.Model):
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name="orders",
        verbose_name="Клиент"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    status = models.CharField(max_length=50, default="Новый", verbose_name="Статус заказа")

    def __str__(self):
        return f"Заказ {self.id} для клиента {self.client}"


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="order_items",
        verbose_name="Заказ"
    )
    price_list = models.ForeignKey(
        PriceList,
        on_delete=models.CASCADE,
        verbose_name="Прайс-лист",
        null=True,
        blank=True
    )
    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество")
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        editable=False,
        verbose_name="Цена за единицу"
    )
    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        editable=False,
        verbose_name="Итоговая стоимость"
    )
    specification_id = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="ID спецификации"
    )

    def calculate_total_price(self):
        """
        Рассчитывает итоговую стоимость на основе прайс-листа и количества.
        """
        if self.price_list:
            self.price = self.price_list.price_default
            self.total_price = self.price * self.quantity
        return self.total_price

    def save(self, *args, **kwargs):
        self.calculate_total_price()
        super().save(*args, **kwargs)

    def __str__(self):
        spec = f" (ID спецификации: {self.specification_id})" if self.specification_id else ""
        return f"Позиция заказа {self.id} — {self.price_list.content_object if self.price_list else 'Нет данных'}{spec}"
