# Generated by Django 3.0.8 on 2021-08-27 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0005_auto_20210825_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='po',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
