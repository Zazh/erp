from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class PriceList(models.Model):
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        verbose_name="Тип объекта"
    )
    object_id = models.PositiveIntegerField(verbose_name="ID объекта")
    content_object = GenericForeignKey('content_type', 'object_id')  # Ссылка на объект (товар или услуга)

    price_individual = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена для Individual",
        null=True,
        blank=True
    )
    price_business = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена для Business",
        null=True,
        blank=True
    )
    price_default = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена по умолчанию",
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "Прайс-лист"
        verbose_name_plural = "Прайс-листы"

    def __str__(self):
        return f"Прайс-лист для {self.content_object}: {self.get_price_display()}"

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
