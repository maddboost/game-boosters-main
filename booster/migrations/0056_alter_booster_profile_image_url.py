# Generated by Django 5.0.4 on 2024-05-05 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booster', '0055_alter_booster_profile_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booster',
            name='profile_image_url',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
    ]
