# Generated by Django 5.1.3 on 2024-11-19 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_alter_orderitem_price_list'),
        ('pricelist', '0002_remove_pricelistproduct_product_variant_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PriceListProduct',
        ),
        migrations.DeleteModel(
            name='PriceListService',
        ),
    ]
