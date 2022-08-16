# Generated by Django 3.2.15 on 2022-08-16 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipts_organizer', '0015_auto_20220816_0718'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='categories',
            name='unique category',
        ),
        migrations.AddConstraint(
            model_name='categories',
            constraint=models.UniqueConstraint(fields=('name', 'user'), name='unique_category'),
        ),
    ]
