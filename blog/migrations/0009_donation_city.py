# Generated by Django 3.1.1 on 2020-10-31 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_donation'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='City',
            field=models.CharField(default='', max_length=100),
        ),
    ]
