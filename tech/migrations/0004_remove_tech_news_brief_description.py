# Generated by Django 3.0.3 on 2020-07-06 02:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0003_auto_20200701_1212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tech_news',
            name='brief_description',
        ),
    ]
