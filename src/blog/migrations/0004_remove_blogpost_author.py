# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-19 20:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogpost_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='author',
        ),
    ]
