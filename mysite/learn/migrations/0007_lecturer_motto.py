# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-06 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0006_lecturer'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecturer',
            name='motto',
            field=models.TextField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
