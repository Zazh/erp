# Generated by Django 5.1.3 on 2024-11-18 19:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Категория')),
            ],
        ),
        migrations.CreateModel(
            name='ProductGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Группа товаров')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_groups', to='products.category', verbose_name='Категория')),
            ],
        ),
        migrations.CreateModel(
            name='ProductTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Шаблон товара')),
                ('product_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_templates', to='products.productgroup', verbose_name='Группа товаров')),
            ],
        ),
        migrations.CreateModel(
            name='ProductVariant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Вариант товара')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category', verbose_name='Категория')),
                ('product_template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_variants', to='products.producttemplate', verbose_name='Шаблон товара')),
            ],
        ),
    ]
