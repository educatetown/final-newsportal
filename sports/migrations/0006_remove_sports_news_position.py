# Generated by Django 3.0.3 on 2020-07-06 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0005_auto_20200706_1310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sports_news',
            name='position',
        ),
    ]
