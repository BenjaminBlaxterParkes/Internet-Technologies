# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-29 18:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0004_auto_20180129_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=0),
            preserve_default=False,
        ),
    ]
