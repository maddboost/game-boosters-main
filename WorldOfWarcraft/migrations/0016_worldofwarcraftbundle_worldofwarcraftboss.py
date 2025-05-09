# Generated by Django 5.0.4 on 2024-07-11 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WorldOfWarcraft', '0015_remove_worldofwarcraftrank_end_rp_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorldOfWarcraftBundle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
                ('price', models.FloatField(default=0)),
                ('image', models.ImageField(upload_to='wow/raid/')),
                ('mode', models.PositiveSmallIntegerField(choices=[(1, 'Raid'), (2, 'Dungeon')])),
                ('feature_1', models.CharField(blank=True, max_length=40, null=True)),
                ('feature_2', models.CharField(blank=True, max_length=40, null=True)),
                ('feature_3', models.CharField(blank=True, max_length=40, null=True)),
                ('feature_4', models.CharField(blank=True, max_length=40, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WorldOfWarcraftBoss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('map', models.PositiveSmallIntegerField(choices=[(1, 'Vault of the Incarnates'), (2, 'Aberrus, the Shadowed Crucible'), (3, "Amirdrassil, the Dream's Hope")])),
                ('name', models.CharField(max_length=100, unique=True)),
                ('price', models.FloatField(default=0)),
            ],
            options={
                'unique_together': {('map', 'name')},
            },
        ),
    ]
