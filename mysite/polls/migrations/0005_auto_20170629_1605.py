# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-29 11:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20170629_0213'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bill',
            options={'verbose_name': 'قبض', 'verbose_name_plural': 'تعریف قبض'},
        ),
        migrations.AlterModelOptions(
            name='billmonth',
            options={'verbose_name': 'قبض', 'verbose_name_plural': 'لیست قبوض'},
        ),
        migrations.AlterModelOptions(
            name='billtype',
            options={'verbose_name': 'نوع قبض', 'verbose_name_plural': 'نوع قبض'},
        ),
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'شهر', 'verbose_name_plural': 'شهر'},
        ),
        migrations.AlterModelOptions(
            name='placetype',
            options={'verbose_name': 'نوع محل', 'verbose_name_plural': 'نوع محل'},
        ),
        migrations.AlterField(
            model_name='billtype',
            name='billtype_name',
            field=models.CharField(max_length=20, verbose_name='نوع قبض'),
        ),
        migrations.AlterField(
            model_name='city',
            name='city_name',
            field=models.CharField(max_length=50, verbose_name='نام شهر'),
        ),
    ]
