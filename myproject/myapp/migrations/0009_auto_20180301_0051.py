# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-02-28 18:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20180301_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='username',
            field=models.CharField(max_length=50),
        ),
    ]