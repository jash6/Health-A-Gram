# Generated by Django 3.1.1 on 2020-11-01 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20201031_1007'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='city',
            new_name='district',
        ),
    ]
