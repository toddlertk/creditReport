# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-27 15:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='timestamp',
        ),
    ]
