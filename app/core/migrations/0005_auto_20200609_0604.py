# Generated by Django 3.0.4 on 2020-06-09 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_recipe'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='time',
            new_name='time_minutes',
        ),
    ]