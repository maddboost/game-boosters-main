# Generated by Django 4.0 on 2024-03-08 02:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0028_alter_room_unique_together_remove_room_booster_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseuser',
            name='last_online',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
