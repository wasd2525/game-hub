# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-28 19:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gamehub', '0004_auto_20170225_1554'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catTitle', models.CharField(db_index=True, max_length=100, null=True)),
                ('slug', models.SlugField(default='Slug', max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(max_length=200),
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gamehub.Category1'),
        ),
    ]
