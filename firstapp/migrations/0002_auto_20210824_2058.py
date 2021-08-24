# Generated by Django 2.1.7 on 2021-08-24 11:58

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prefectures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'prefectures',
            },
        ),
        migrations.CreateModel(
            name='Schools',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('prefecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.Prefectures')),
            ],
            options={
                'db_table': 'schools',
            },
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('major', models.CharField(max_length=30)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.Schools')),
            ],
            options={
                'db_table': 'students',
            },
        ),
        migrations.AlterModelOptions(
            name='language',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='language',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 24, 11, 58, 33, 80578, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='language',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 24, 11, 58, 33, 80637, tzinfo=utc)),
        ),
    ]