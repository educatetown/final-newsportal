# Generated by Django 3.0.3 on 2020-06-21 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsportalapp', '0002_news_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='position',
            field=models.CharField(choices=[('First_left', 'first_left'), ('First_right', 'first_right'), ('Second_left', 'second_left'), ('Second_right', 'second_right'), ('Third_left', 'third_left'), ('Third_right', 'third_right')], default='First_left', max_length=30),
        ),
    ]
