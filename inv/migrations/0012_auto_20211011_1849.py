# Generated by Django 3.0.8 on 2021-10-11 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0011_auto_20211011_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalitem',
            name='item_description',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_description',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]
