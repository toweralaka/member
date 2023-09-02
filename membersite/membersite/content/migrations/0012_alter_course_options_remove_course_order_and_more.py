# Generated by Django 4.0.10 on 2023-09-02 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0011_pricing_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={},
        ),
        migrations.RemoveField(
            model_name='course',
            name='order',
        ),
        migrations.AddField(
            model_name='pricing',
            name='stripe_price_id',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='video',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
