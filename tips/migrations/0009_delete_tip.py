# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-29 13:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tips', '0008_auto_20160629_2110'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tip',
        ),
    ]
