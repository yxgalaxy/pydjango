# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-01 02:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0005_book_tags_chapter_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book_chapter',
            options={'verbose_name': '书目章节', 'verbose_name_plural': '书目章节'},
        ),
        migrations.AlterModelOptions(
            name='book_name',
            options={'verbose_name': '书名', 'verbose_name_plural': '书名'},
        ),
        migrations.AlterModelOptions(
            name='book_tags',
            options={'verbose_name': '标签云', 'verbose_name_plural': '标签云'},
        ),
        migrations.RemoveField(
            model_name='book_name',
            name='time',
        ),
        migrations.AddField(
            model_name='book_name',
            name='add_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='保存日期'),
        ),
        migrations.AddField(
            model_name='book_name',
            name='mod_date',
            field=models.DateTimeField(auto_now=True, verbose_name='最后修改日期'),
        ),
    ]
