# Generated by Django 5.1.4 on 2025-01-14 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_remove_order_detail_courier_charges_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_detail',
            name='total_price',
            field=models.FloatField(default=0),
        ),
    ]
