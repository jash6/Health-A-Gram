# Generated by Django 3.1.1 on 2020-10-31 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20201031_0637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donordetails',
            name='anemia',
            field=models.CharField(default='no', max_length=10),
        ),
        migrations.AlterField(
            model_name='donordetails',
            name='covid',
            field=models.CharField(default='yes', max_length=10),
        ),
        migrations.AlterField(
            model_name='donordetails',
            name='days',
            field=models.CharField(default='14', max_length=10),
        ),
        migrations.AlterField(
            model_name='donordetails',
            name='doctors_prescription',
            field=models.ImageField(default='default.jpg', upload_to='prescription_pics'),
        ),
        migrations.AlterField(
            model_name='donordetails',
            name='infectious_diseases',
            field=models.CharField(default='no', max_length=10),
        ),
        migrations.AlterField(
            model_name='donordetails',
            name='pregnant',
            field=models.CharField(default='no', max_length=10),
        ),
        migrations.AlterField(
            model_name='donordetails',
            name='test',
            field=models.CharField(default='yes', max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='is_donor',
            field=models.BooleanField(default=False),
        ),
    ]
