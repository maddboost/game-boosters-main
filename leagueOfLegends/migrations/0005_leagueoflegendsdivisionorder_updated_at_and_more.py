# Generated by Django 4.2.7 on 2024-04-13 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leagueOfLegends', '0004_leagueoflegendsdivisionorder_champions_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='leagueoflegendsdivisionorder',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='leagueoflegendsplacementorder',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
