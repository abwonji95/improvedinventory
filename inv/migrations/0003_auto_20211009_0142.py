# Generated by Django 3.0.8 on 2021-10-09 01:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0002_auto_20211009_0025'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalpurchase',
            name='items',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='inv.Item'),
        ),
        migrations.AddField(
            model_name='purchase',
            name='items',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inv.Item'),
        ),
    ]
