# Generated by Django 3.1 on 2020-09-07 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20200907_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_id_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.categories'),
            preserve_default=False,
        ),
    ]
