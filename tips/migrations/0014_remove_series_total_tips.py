# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-29 13:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tips', '0013_tip'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='series',
            name='total_tips',
        ),
    ]
