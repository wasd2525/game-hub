# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 12:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamehub', '0004_auto_20170225_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(max_length=200),
        ),
    ]