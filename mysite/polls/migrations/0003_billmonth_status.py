# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-12 15:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20170612_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='billmonth',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
