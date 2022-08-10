# Generated by Django 3.2.15 on 2022-08-10 10:09

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receipts_organizer', '0004_alter_categories_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entries',
            name='image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]