# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-30 07:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamehub', '0009_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='Slug', max_length=100),
        ),
    ]
