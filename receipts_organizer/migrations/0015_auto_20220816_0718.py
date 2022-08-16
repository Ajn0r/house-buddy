# Generated by Django 3.2.15 on 2022-08-16 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipts_organizer', '0014_alter_categories_name'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='categories',
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name='categories',
            constraint=models.UniqueConstraint(fields=('name', 'user'), name='unique category'),
        ),
    ]
