# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-15 01:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaint', '0005_auto_20180715_0152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='photo',
            field=models.ImageField(default='media/borat.jpg', upload_to='complaints/', verbose_name='Фото'),
        ),
    ]
