# Generated by Django 5.0.4 on 2024-07-15 03:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WorldOfWarcraft', '0016_worldofwarcraftbundle_worldofwarcraftboss'),
        ('accounts', '0060_alter_baseorder_game_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorldOfWarcraftRaidSimpleOrder',
            fields=[
                ('order', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='wow_raid_simple_order', serialize=False, to='accounts.baseorder')),
                ('map', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Vault of the Incarnates'), (2, 'Aberrus, the Shadowed Crucible'), (3, "Amirdrassil, the Dream's Hope")], null=True)),
                ('difficulty', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('bosses', models.ManyToManyField(related_name='wow_raid_simple_order_bosses', to='WorldOfWarcraft.worldofwarcraftboss')),
            ],
        ),
    ]
