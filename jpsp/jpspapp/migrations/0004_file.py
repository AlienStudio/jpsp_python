# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-19 15:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jpspapp.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jpspapp', '0003_auto_20170809_1216'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='文件名', max_length=30, unique=True)),
                ('Datetime', models.DateTimeField(auto_now_add=True)),
                ('File', models.FileField(upload_to=jpspapp.models.file_directory_path)),
                ('UserObject', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]