# Generated by Django 3.0.8 on 2021-10-14 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0015_auto_20211013_1650'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('code', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('code', models.CharField(max_length=64)),
                ('price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inv.ProductCategory')),
            ],
        ),
    ]
