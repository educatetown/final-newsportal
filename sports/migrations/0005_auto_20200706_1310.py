# Generated by Django 3.0.3 on 2020-07-06 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0004_remove_sports_news_published_other_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sports_news',
            name='published_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
