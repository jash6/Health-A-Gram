# Generated by Django 3.1.1 on 2020-10-31 06:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('gender', models.CharField(default='', max_length=10)),
                ('age', models.IntegerField(default=1)),
                ('blood_group', models.CharField(default='', max_length=50)),
                ('city', models.CharField(default='', max_length=10)),
                ('Hospital', models.CharField(default='', max_length=10)),
                ('has_corona', models.CharField(default='', max_length=10)),
                ('is_donor', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DonorDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField(default=1)),
                ('pregnant', models.CharField(default='no', max_length=10)),
                ('anemia', models.CharField(default='no', max_length=10)),
                ('infectious_diseases', models.CharField(default='no', max_length=10)),
                ('doctors_prescription', models.CharField(default='yes', max_length=10)),
                ('days', models.CharField(default='14', max_length=10)),
                ('test', models.CharField(default='yes', max_length=10)),
                ('covid', models.CharField(default='yes', max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
    ]
