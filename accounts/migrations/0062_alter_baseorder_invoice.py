# Generated by Django 5.0.4 on 2024-09-07 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0061_alter_tokenforpay_invoice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseorder',
            name='invoice',
            field=models.CharField(max_length=2000),
        ),
    ]
