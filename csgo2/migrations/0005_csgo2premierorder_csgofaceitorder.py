# Generated by Django 4.2.7 on 2024-03-17 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csgo2', '0004_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Csgo2PremierOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='CsgoFaceitOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
