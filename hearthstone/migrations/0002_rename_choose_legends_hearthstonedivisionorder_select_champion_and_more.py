# Generated by Django 4.2.7 on 2024-03-05 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hearthstone', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hearthstonedivisionorder',
            old_name='choose_legends',
            new_name='select_champion',
        ),
        migrations.RemoveField(
            model_name='hearthstonedivisionorder',
            name='speed_up_boost',
        ),
        migrations.AlterField(
            model_name='hearthstonedivisionorder',
            name='current_division',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'X'), (2, 'IX'), (3, 'VIII'), (4, 'VII'), (5, 'VI'), (6, 'V'), (7, 'IV'), (8, 'III'), (9, 'II'), (10, 'I')], null=True),
        ),
        migrations.AlterField(
            model_name='hearthstonedivisionorder',
            name='current_marks',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, '3'), (1, '2'), (2, '1')], null=True),
        ),
        migrations.AlterField(
            model_name='hearthstonedivisionorder',
            name='desired_division',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'X'), (2, 'IX'), (3, 'VIII'), (4, 'VII'), (5, 'VI'), (6, 'V'), (7, 'IV'), (8, 'III'), (9, 'II'), (10, 'I')], null=True),
        ),
        migrations.AlterField(
            model_name='hearthstonedivisionorder',
            name='reached_division',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'X'), (2, 'IX'), (3, 'VIII'), (4, 'VII'), (5, 'VI'), (6, 'V'), (7, 'IV'), (8, 'III'), (9, 'II'), (10, 'I')], null=True),
        ),
        migrations.AlterField(
            model_name='hearthstonedivisionorder',
            name='reached_marks',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, '3'), (1, '2'), (2, '1')], null=True),
        ),
    ]
