# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-26 08:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book_name',
            fields=[
                ('id', models.AutoField(max_length=11, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, verbose_name='书名')),
                ('author', models.CharField(max_length=30, verbose_name='作者')),
                ('time', models.CharField(max_length=30, verbose_name='时间')),
            ],
            options={
                'verbose_name': '书名',
                'verbose_name_plural': '作者',
            },
        ),
        migrations.CreateModel(
            name='book_tags',
            fields=[
                ('id', models.AutoField(max_length=11, primary_key=True, serialize=False)),
                ('book_id', models.IntegerField(verbose_name='书目id')),
                ('text', models.TextField(max_length=140, verbose_name='标签')),
            ],
        ),
    ]
