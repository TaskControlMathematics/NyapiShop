# Generated by Django 3.1 on 2020-09-03 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20200815_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordforgot',
            name='email',
            field=models.CharField(max_length=256),
        ),
    ]
