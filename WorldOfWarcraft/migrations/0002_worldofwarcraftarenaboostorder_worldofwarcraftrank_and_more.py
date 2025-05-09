# Generated by Django 4.0 on 2024-03-07 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_remove_baseorder_game_id_remove_baseorder_game_name_and_more'),
        ('WorldOfWarcraft', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorldOfWarcraftArenaBoostOrder',
            fields=[
                ('is_Arena_2x2', models.BooleanField(default=True)),
                ('order', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='wow_division_order', serialize=False, to='accounts.baseorder')),
                ('current_division', models.IntegerField(default=0)),
                ('reached_division', models.IntegerField(default=0)),
                ('desired_division', models.IntegerField(default=25)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('choose_champions', models.BooleanField(blank=True, default=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WorldOfWarcraftRank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank_name', models.CharField(max_length=25)),
                ('rank_image', models.ImageField(blank=True, null=True, upload_to='wow/images/')),
                ('start_RP', models.IntegerField()),
                ('end_RP', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='WorldOfWarcraftRpsPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_of_2vs2', models.IntegerField(default=1)),
                ('price_of_3vs3', models.IntegerField(default=2)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='WoW_25_RPs_Price_2x2',
        ),
        migrations.DeleteModel(
            name='WoW_25_RPs_Price_3x3',
        ),
        migrations.DeleteModel(
            name='WoWArenaBoostOrder',
        ),
    ]
