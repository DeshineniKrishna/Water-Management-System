# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-09 18:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='humidity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hum_value', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='soilmoisture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soil_value', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='temperature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tem_value', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='waterlevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('water_level', models.CharField(max_length=250)),
            ],
        ),
        migrations.DeleteModel(
            name='sensor',
        ),
    ]
