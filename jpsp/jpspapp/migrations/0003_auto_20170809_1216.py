# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-09 12:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jpspapp', '0002_auto_20170808_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='Email',
            field=models.EmailField(default='123@123.com', max_length=254),
        ),
    ]
