# Generated by Django 4.2.7 on 2024-04-15 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rocketLeague', '0004_rocketleagueplacementorder_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='RocketLeaguePlacement1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank_name', models.CharField(max_length=25)),
                ('rank_image', models.ImageField(blank=True, null=True, upload_to='rocketLeague/images/')),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='RocketLeagueRank1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank_name', models.CharField(max_length=25)),
                ('rank_image', models.ImageField(blank=True, null=True, upload_to='rocketLeague/images/')),
            ],
        ),
        migrations.CreateModel(
            name='RocketLeagueSeasonal1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank_name', models.CharField(max_length=25)),
                ('rank_image', models.ImageField(blank=True, null=True, upload_to='rocketLeague/images/')),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='RocketLeagueTournament1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank_name', models.CharField(max_length=25)),
                ('rank_image', models.ImageField(blank=True, null=True, upload_to='rocketLeague/images/')),
                ('price', models.FloatField()),
            ],
        ),
        migrations.AlterField(
            model_name='rocketleaguedivision',
            name='rank',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='tier', to='rocketLeague.rocketleaguerank1'),
        ),
        migrations.AlterField(
            model_name='rocketleaguedivisionorder',
            name='current_rank',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='current_rank', to='rocketLeague.rocketleaguerank1'),
        ),
        migrations.AlterField(
            model_name='rocketleaguedivisionorder',
            name='desired_rank',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='desired_rank', to='rocketLeague.rocketleaguerank1'),
        ),
        migrations.AlterField(
            model_name='rocketleaguedivisionorder',
            name='reached_rank',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reached_rank', to='rocketLeague.rocketleaguerank1'),
        ),
        migrations.AlterField(
            model_name='rocketleagueplacementorder',
            name='last_rank',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='last_rank', to='rocketLeague.rocketleagueplacement1'),
        ),
        migrations.AlterField(
            model_name='rocketleagueseasonalorder',
            name='current_rank',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='current_rank', to='rocketLeague.rocketleagueseasonal1'),
        ),
        migrations.AlterField(
            model_name='rocketleaguetournamentorder',
            name='current_league',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='current_league', to='rocketLeague.rocketleaguetournament1'),
        ),
        migrations.DeleteModel(
            name='RocketLeaguePlacement',
        ),
    ]
