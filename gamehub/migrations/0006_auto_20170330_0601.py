# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-30 06:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamehub', '0005_auto_20170328_1958'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='catTitle',
            field=models.CharField(db_index=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='Slug', max_length=100),
        ),
    ]
