from django.db import models

# Категория товара
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Категория")

    def __str__(self):
        return self.name

# Группа товаров
class ProductGroup(models.Model):
    name = models.CharField(max_length=100, verbose_name="Группа товаров")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="product_groups", verbose_name="Категория")

    def __str__(self):
        return f"{self.name} ({self.category.name})"

# Шаблон товара (Product Template)
class ProductTemplate(models.Model):
    name = models.CharField(max_length=100, verbose_name="Шаблон товара")
    product_group = models.ForeignKey(ProductGroup, on_delete=models.CASCADE, related_name="product_templates", verbose_name="Группа товаров")

    def __str__(self):
        return self.name

# Вариант товара (Product Variant)
class ProductVariant(models.Model):
    name = models.CharField(max_length=150, verbose_name="Вариант товара")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    product_template = models.ForeignKey(ProductTemplate, on_delete=models.CASCADE, related_name="product_variants", verbose_name="Шаблон товара")

    def __str__(self):
        return self.name
