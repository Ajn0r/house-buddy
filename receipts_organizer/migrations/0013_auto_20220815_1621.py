# Generated by Django 3.2.15 on 2022-08-15 16:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('receipts_organizer', '0012_alter_categories_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='slug',
            field=models.SlugField(max_length=200),
        ),
        migrations.AlterUniqueTogether(
            name='categories',
            unique_together={('name', 'user')},
        ),
    ]
