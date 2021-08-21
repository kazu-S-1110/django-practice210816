# Generated by Django 2.1.7 on 2021-08-21 03:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_framework'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 21, 12, 24, 5, 513955)),
        ),
        migrations.AddField(
            model_name='language',
            name='email',
            field=models.EmailField(db_index=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='language',
            name='memo',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='language',
            name='salary',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='language',
            name='startday',
            field=models.DateField(default='2000-01-01'),
        ),
        migrations.AddField(
            model_name='language',
            name='web_site',
            field=models.URLField(blank=True, null=True),
        ),
    ]
