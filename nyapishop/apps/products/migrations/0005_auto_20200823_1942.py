# Generated by Django 3.1 on 2020-08-23 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200818_1806'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['product_title'], 'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
    ]
