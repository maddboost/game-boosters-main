# Generated by Django 5.0.4 on 2024-06-02 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_alter_message_msg_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='msg_type',
            field=models.IntegerField(choices=[(1, 'normal'), (2, 'tip'), (3, 'changes'), (4, 'admin'), (5, 'refresh')], default=1),
        ),
    ]
