# Generated by Django 3.1 on 2020-09-07 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='id_parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.categories'),
        ),
    ]
