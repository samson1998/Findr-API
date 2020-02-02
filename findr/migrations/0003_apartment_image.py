# Generated by Django 3.0 on 2020-01-31 11:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('findr', '0002_auto_20200113_1158'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_pic', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('house_address', models.CharField(max_length=10000, verbose_name='house_address')),
                ('house_name', models.CharField(max_length=60, verbose_name='house_name')),
                ('title', models.CharField(max_length=300)),
                ('price', models.CharField(max_length=60, verbose_name='price')),
                ('isFurnished', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=50, verbose_name='furnished')),
                ('isParkingSpace', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=70, verbose_name='parkingspace')),
                ('isAvailable', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=100, verbose_name='available')),
                ('isFenced', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=100, verbose_name='fenced')),
                ('isHaveWater', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=100, verbose_name='water')),
                ('isNewHouse', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=80, verbose_name='new')),
                ('isNegotiable', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=80, verbose_name='Negotiable')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='findr.Image')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
