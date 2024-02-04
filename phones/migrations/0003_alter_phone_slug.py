# Generated by Django 5.0.1 on 2024-02-03 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0002_phone_lte_exists_phone_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='slug',
            field=models.SlugField(default='', max_length=255, unique=True, verbose_name='URL'),
        ),
    ]