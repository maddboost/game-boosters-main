# Generated by Django 5.0.4 on 2024-09-22 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0067_rename_tokenforpay2_tokenforpay'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tokenforpay',
            name='game_info',
            field=models.TextField(max_length=2000),
        ),
    ]
