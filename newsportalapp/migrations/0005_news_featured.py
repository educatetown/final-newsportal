# Generated by Django 3.0.3 on 2020-06-27 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsportalapp', '0004_news_event_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
