# Generated by Django 3.0.8 on 2021-10-09 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalitem',
            name='item_description',
            field=models.TextField(blank=True, default='Item description', max_length=200),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_description',
            field=models.TextField(blank=True, default='Item description', max_length=200),
        ),
    ]
