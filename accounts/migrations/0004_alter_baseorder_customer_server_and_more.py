# Generated by Django 4.2.7 on 2024-02-21 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_baseorder_customer_server'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseorder',
            name='customer_server',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='baseorder',
            name='game_type',
            field=models.CharField(choices=[('D', 'Division'), ('P', 'Placement'), ('A', 'Arena')], max_length=10, null=True),
        ),
    ]
