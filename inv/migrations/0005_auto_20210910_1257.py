# Generated by Django 3.0.8 on 2021-09-10 12:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0004_remove_purchasedetails_vendor'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalpurchase',
            name='price',
            field=models.FloatField(blank=True, default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='historicalpurchase',
            name='purchased_qty',
            field=models.IntegerField(blank=True, default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='purchase',
            name='price',
            field=models.FloatField(blank=True, default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='purchase',
            name='purchased_qty',
            field=models.IntegerField(blank=True, default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
