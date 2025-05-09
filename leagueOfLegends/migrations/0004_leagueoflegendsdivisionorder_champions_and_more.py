# Generated by Django 4.2.7 on 2024-03-31 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0008_champion_delete_championc'),
        ('leagueOfLegends', '0003_rename_choose_champions_leagueoflegendsplacementorder_select_champion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='leagueoflegendsdivisionorder',
            name='champions',
            field=models.ManyToManyField(blank=True, related_name='lol_division_champions', to='customer.champion'),
        ),
        migrations.AddField(
            model_name='leagueoflegendsplacementorder',
            name='champions',
            field=models.ManyToManyField(blank=True, related_name='lol_placement_champions', to='customer.champion'),
        ),
    ]
