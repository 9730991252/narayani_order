# Generated by Django 5.1.4 on 2025-03-22 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0009_rattings'),
    ]

    operations = [
        migrations.AddField(
            model_name='rattings',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='rattings',
            name='reviev_description',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='rattings',
            name='reviev_title',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
