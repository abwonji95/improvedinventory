# Generated by Django 3.0.8 on 2021-08-30 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0007_delete_productreturn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuance',
            name='issuedto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inv.Engineer'),
        ),
    ]
