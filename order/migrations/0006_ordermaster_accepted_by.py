# Generated by Django 5.1.4 on 2025-01-13 10:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_remove_order_detail_total_price'),
        ('sunil', '0002_employee_delete_shope'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermaster',
            name='accepted_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='sunil.employee'),
        ),
    ]
