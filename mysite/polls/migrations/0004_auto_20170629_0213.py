# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-28 21:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_billmonth_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placetype',
            name='placetype_name',
            field=models.CharField(max_length=50, verbose_name='نوع مکان'),
        ),
    ]