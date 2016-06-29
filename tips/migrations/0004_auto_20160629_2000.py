# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-29 12:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tips', '0003_auto_20160629_1050'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tip',
            old_name='created_at',
            new_name='pub_date',
        ),
        migrations.AddField(
            model_name='tip',
            name='author',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='tip',
            name='resources',
            field=models.TextField(default=''),
        ),
    ]
