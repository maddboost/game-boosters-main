# Generated by Django 5.0.4 on 2024-04-30 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobileLegends', '0013_mobilelegendsplacementorder_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobilelegendsplacement',
            name='rank_image',
            field=models.ImageField(blank=True, null=True, upload_to='mobile_legends/images/'),
        ),
    ]
