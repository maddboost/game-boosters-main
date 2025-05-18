from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WorldOfWarcraft', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='worldofwarcraftarenaboostorder',
            name='rank1_player',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='worldofwarcraftarenaboostorder',
            name='tournament_player',
            field=models.BooleanField(default=False),
        ),
    ]
