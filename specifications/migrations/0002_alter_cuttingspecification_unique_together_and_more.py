# Generated by Django 5.1.3 on 2024-11-18 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('specifications', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cuttingspecification',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='edgingspecification',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='facadespecification',
            unique_together=set(),
        ),
    ]
