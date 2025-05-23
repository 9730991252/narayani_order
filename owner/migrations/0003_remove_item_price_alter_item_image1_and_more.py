# Generated by Django 5.1.4 on 2025-01-12 03:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0002_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='price',
        ),
        migrations.AlterField(
            model_name='item',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='item_images/'),
        ),
        migrations.AlterField(
            model_name='item',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='item_images/'),
        ),
        migrations.AlterField(
            model_name='item',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='item_images/'),
        ),
        migrations.AlterField(
            model_name='item',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='item_images/'),
        ),
        migrations.AlterField(
            model_name='item',
            name='image5',
            field=models.ImageField(blank=True, null=True, upload_to='item_images/'),
        ),
        migrations.CreateModel(
            name='Price_and_weight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prise', models.FloatField()),
                ('weight', models.IntegerField()),
                ('unit', models.CharField(max_length=100)),
                ('status', models.IntegerField(default=1)),
                ('iteme', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='owner.item')),
            ],
        ),
    ]
