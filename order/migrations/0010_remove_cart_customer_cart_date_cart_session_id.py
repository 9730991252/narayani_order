# Generated by Django 5.1.4 on 2025-02-15 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_remove_order_detail_total_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='customer',
        ),
        migrations.AddField(
            model_name='cart',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='session_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
