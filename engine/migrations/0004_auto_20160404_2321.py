# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-04 23:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0003_auto_20160403_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='abbreviation',
            field=models.CharField(max_length=2),
        ),
    ]
