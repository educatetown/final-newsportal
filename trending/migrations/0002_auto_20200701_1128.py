# Generated by Django 3.0.3 on 2020-07-01 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trending', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trending_news',
            name='event_place',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='trending_news',
            name='published_at',
            field=models.DateTimeField(),
        ),
    ]
