# Generated by Django 4.2.7 on 2024-03-05 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mobileLegends', '0009_alter_mobilelegendsdivisionorder_current_marks_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mobilelegendsdivisionorder',
            old_name='choose_champions',
            new_name='select_champion',
        ),
        migrations.RenameField(
            model_name='mobilelegendsplacementorder',
            old_name='choose_champions',
            new_name='select_champion',
        ),
    ]
