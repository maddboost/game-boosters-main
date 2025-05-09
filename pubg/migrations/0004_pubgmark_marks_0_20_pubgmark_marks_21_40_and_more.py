# Generated by Django 4.2.7 on 2024-03-13 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pubg', '0003_remove_pubgmark_marks_0_20_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pubgmark',
            name='marks_0_20',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='pubgmark',
            name='marks_21_40',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='pubgmark',
            name='marks_41_60',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='pubgmark',
            name='marks_61_80',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='pubgmark',
            name='marks_81_100',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='pubgmark',
            name='rank',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mark', to='pubg.pubgrank'),
        ),
        migrations.AddField(
            model_name='pubgrank',
            name='rank_image',
            field=models.ImageField(blank=True, null=True, upload_to='pubg/images/'),
        ),
        migrations.AddField(
            model_name='pubgrank',
            name='rank_name',
            field=models.CharField(default='rank name', max_length=25),
        ),
        migrations.AddField(
            model_name='pubgtier',
            name='from_III_to_II',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='pubgtier',
            name='from_II_to_I',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='pubgtier',
            name='from_I_to_V_next',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='pubgtier',
            name='from_VI_to_III',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='pubgtier',
            name='from_V_to_VI',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='pubgtier',
            name='rank',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tier', to='pubg.pubgrank'),
        ),
    ]
