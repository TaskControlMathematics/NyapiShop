# Generated by Django 3.1 on 2020-09-22 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_productinbasket_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinbasket',
            name='images',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
