# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-02-28 18:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_auto_20180301_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='ans',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='questions',
            name='ques',
            field=models.CharField(max_length=2000),
        ),
    ]
