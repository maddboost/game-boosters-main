# Generated by Django 5.0.4 on 2024-05-06 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0050_alter_baseorder_wins_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseorder',
            name='wins_number',
            field=models.PositiveSmallIntegerField(blank=True, default=0),
        ),
    ]
