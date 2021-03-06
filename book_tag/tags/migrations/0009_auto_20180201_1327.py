# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-01 05:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0008_book_tags_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_name',
            name='brief',
            field=models.TextField(max_length=500, verbose_name='简介'),
        ),
        migrations.AlterField(
            model_name='book_tags',
            name='name',
            field=models.CharField(max_length=30, verbose_name='标签'),
        ),
        migrations.AlterField(
            model_name='book_tags',
            name='text',
            field=models.TextField(max_length=140, verbose_name='具体描述'),
        ),
    ]
