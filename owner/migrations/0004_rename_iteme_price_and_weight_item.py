# Generated by Django 5.1.4 on 2025-01-12 03:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0003_remove_item_price_alter_item_image1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='price_and_weight',
            old_name='iteme',
            new_name='item',
        ),
    ]