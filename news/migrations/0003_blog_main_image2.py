# Generated by Django 5.0.4 on 2024-05-30 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_blog_order_image2'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='main_image2',
            field=models.ImageField(default='', upload_to='blog/'),
            preserve_default=False,
        ),
    ]
