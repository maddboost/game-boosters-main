# Generated by Django 4.2.7 on 2024-02-28 03:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_alter_baseorder_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='name',
        ),
        migrations.RemoveField(
            model_name='room',
            name='order',
        ),
        migrations.AddField(
            model_name='room',
            name='is_for_admins',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='order_name',
            field=models.CharField(default='order_name', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tip_data',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tip_data',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='tokenforpay',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tokenforpay',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='msg_type',
            field=models.IntegerField(choices=[(1, 'normal'), (2, 'tip')], default=1),
        ),
        migrations.AlterField(
            model_name='room',
            name='customer',
            field=models.ForeignKey(blank=True, default=None, limit_choices_to={'is_booster': False}, on_delete=django.db.models.deletion.DO_NOTHING, related_name='customer_room', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tip_data',
            name='invoice',
            field=models.TextField(default='invoice', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tip_data',
            name='payer_id',
            field=models.CharField(default='payer_id', max_length=50),
            preserve_default=False,
        ),
    ]
