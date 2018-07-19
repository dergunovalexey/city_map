# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-19 07:04
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trackrecorder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roadtreck',
            name='accselerometer_points',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), size=None),
        ),
        migrations.AlterField(
            model_name='roadtreck',
            name='magnetometer_points',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), size=None),
        ),
    ]
