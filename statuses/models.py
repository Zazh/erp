from django.db import models

class StatusCategory(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Категория статусов")
    description = models.TextField(blank=True, null=True, verbose_name="Описание категории")

    def __str__(self):
        return self.name

class Status(models.Model):
    category = models.ForeignKey(StatusCategory, on_delete=models.CASCADE, related_name="statuses", verbose_name="Категория")
    name = models.CharField(max_length=100, unique=True, verbose_name="Наименование статуса")
    description = models.TextField(blank=True, null=True, verbose_name="Описание статуса")
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    color = models.CharField(max_length=7, default="#000000", verbose_name="Цвет статуса (HEX)")

    def __str__(self):
        return f"{self.name} ({self.category.name})"
