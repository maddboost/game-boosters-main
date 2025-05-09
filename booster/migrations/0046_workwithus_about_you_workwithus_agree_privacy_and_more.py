# Generated by Django 5.0.4 on 2024-04-27 08:22

import django_countries.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booster', '0045_createbooster_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='workwithus',
            name='about_you',
            field=models.TextField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workwithus',
            name='agree_privacy',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='workwithus',
            name='country',
            field=django_countries.fields.CountryField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='workwithus',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]
