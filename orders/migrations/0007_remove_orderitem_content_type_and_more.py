# Generated by Django 5.1.3 on 2024-11-20 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_rename_specification_type_orderitem_content_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='specification_id',
        ),
    ]
