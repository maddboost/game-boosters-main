# Generated by Django 5.0.4 on 2025-05-16 11:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Overwatch2Placement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank_name', models.CharField(max_length=25)),
                ('rank_image', models.ImageField(blank=True, null=True, upload_to='overwatch2/images/')),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Overwatch2Rank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank_name', models.CharField(max_length=25)),
                ('rank_image', models.ImageField(blank=True, null=True, upload_to='overwatch2/images/')),
            ],
        ),
        migrations.CreateModel(
            name='Overwatch2PlacementOrder',
            fields=[
                ('order', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='ovw2_placement_order', serialize=False, to='accounts.baseorder')),
                ('number_of_match', models.IntegerField(default=5)),
                ('role', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'DPS'), (2, 'TANK'), (3, 'SUPPORT')], default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('select_champions', models.BooleanField(blank=True, default=False, null=True)),
                ('last_rank', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='ovw2_last_rank', to='overwatch2.overwatch2placement')),
            ],
        ),
        migrations.CreateModel(
            name='Overwatch2Mark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark_number', models.PositiveSmallIntegerField(default=5)),
                ('mark_1', models.FloatField(default=0)),
                ('mark_2', models.FloatField(default=0)),
                ('mark_3', models.FloatField(default=0)),
                ('mark_4', models.FloatField(default=0)),
                ('mark_5', models.FloatField(default=0)),
                ('rank', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='mark', to='overwatch2.overwatch2rank')),
            ],
        ),
        migrations.CreateModel(
            name='Overwatch2DivisionOrder',
            fields=[
                ('order', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='overwatch2_order', serialize=False, to='accounts.baseorder')),
                ('current_division', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'V'), (2, 'IV'), (3, 'III'), (4, 'II'), (5, 'I')])),
                ('reached_division', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'V'), (2, 'IV'), (3, 'III'), (4, 'II'), (5, 'I')], null=True)),
                ('desired_division', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'V'), (2, 'IV'), (3, 'III'), (4, 'II'), (5, 'I')])),
                ('current_marks', models.PositiveSmallIntegerField(blank=True, choices=[(1, '0-19 %'), (2, '20-39 %'), (3, '40-59 %'), (4, '60-79 %'), (5, '80-99 %')])),
                ('reached_marks', models.PositiveSmallIntegerField(blank=True, choices=[(1, '0-19 %'), (2, '20-39 %'), (3, '40-59 %'), (4, '60-79 %'), (5, '80-99 %')], null=True)),
                ('role', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'DPS'), (2, 'TANK'), (3, 'SUPPORT')], default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('current_rank', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.PROTECT, related_name='current_rank', to='overwatch2.overwatch2rank')),
                ('desired_rank', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.PROTECT, related_name='desired_rank', to='overwatch2.overwatch2rank')),
                ('reached_rank', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='reached_rank', to='overwatch2.overwatch2rank')),
            ],
        ),
        migrations.CreateModel(
            name='Overwatch2Tier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_V_to_IV', models.FloatField(default=0)),
                ('from_IV_to_III', models.FloatField(default=0)),
                ('from_III_to_II', models.FloatField(default=0)),
                ('from_II_to_I', models.FloatField(default=0)),
                ('from_I_to_V_next', models.FloatField(default=0)),
                ('rank', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='tier', to='overwatch2.overwatch2rank')),
            ],
        ),
    ]
