# Generated by Django 3.1 on 2020-08-23 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20200823_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_title',
            field=models.CharField(max_length=200, verbose_name='product_title'),
        ),
    ]
