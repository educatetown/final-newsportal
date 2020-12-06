# Generated by Django 3.0.3 on 2020-06-27 03:55

from django.db import migrations, models
import trending.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trending_News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=255)),
                ('reporter', models.CharField(blank=True, max_length=50, null=True)),
                ('brief_description', models.TextField()),
                ('description', models.TextField()),
                ('picture1', models.ImageField(blank=True, null=True, upload_to=trending.models.upload_location)),
                ('picture2', models.ImageField(blank=True, null=True, upload_to=trending.models.upload_location)),
                ('picture3', models.ImageField(blank=True, null=True, upload_to=trending.models.upload_location)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to=trending.models.upload_location)),
                ('published_at', models.DateTimeField(auto_now=True)),
                ('published_other_date', models.DateTimeField(blank=True, null=True)),
                ('position', models.CharField(choices=[('First_left', 'first_left'), ('First_right', 'first_right'), ('Second_left', 'second_left'), ('Second_right', 'second_right'), ('Third_left', 'third_left'), ('Third_right', 'third_right')], default='First_left', max_length=30)),
                ('slug', models.SlugField(allow_unicode=True, blank=True, null=True, unique=True)),
            ],
        ),
    ]
