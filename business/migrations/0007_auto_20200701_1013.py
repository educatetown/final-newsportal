# Generated by Django 3.0.3 on 2020-07-01 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0006_auto_20200701_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business_news',
            name='published_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
