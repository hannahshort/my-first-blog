# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-27 16:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.PositiveSmallIntegerField(blank=True, default=0, editable=False, null=True),
        ),
    ]
