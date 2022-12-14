# Generated by Django 3.2.15 on 2022-08-20 10:04

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipts_organizer', '0017_alter_entries_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entries',
            name='amount',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='entries',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, default='no_image', max_length=255, null=True, verbose_name='image'),
        ),
    ]
