# Generated by Django 3.2.15 on 2022-08-15 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipts_organizer', '0013_auto_20220815_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
