# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-02-23 13:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Directors',
            new_name='UserInfo',
        ),
    ]
