# Generated by Django 5.0.4 on 2024-04-24 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booster', '0044_createbooster_is_csgo2_player_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='createbooster',
            name='email',
            field=models.EmailField(default='ali@ali.com', max_length=150),
            preserve_default=False,
        ),
    ]
