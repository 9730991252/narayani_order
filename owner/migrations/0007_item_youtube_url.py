# Generated by Django 5.1.4 on 2025-01-14 03:39

import embed_video.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0006_category_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='youtube_url',
            field=embed_video.fields.EmbedVideoField(null=True),
        ),
    ]
