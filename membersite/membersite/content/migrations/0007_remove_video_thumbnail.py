# Generated by Django 4.0.10 on 2023-05-07 23:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0006_video_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='thumbnail',
        ),
    ]
