# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-09 01:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0006_auto_20170908_1306'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Db',
            new_name='Information',
        ),
    ]
