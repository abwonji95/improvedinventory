# Generated by Django 3.0.8 on 2021-09-08 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0007_auto_20210908_1303'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicalstock',
            old_name='returneditems_qty',
            new_name='returned_qty',
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='returneditems_qty',
            new_name='returned_qty',
        ),
    ]
