# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-10-11 19:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('question_game', '0008_auto_20181011_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 11, 19, 12, 46, 667329, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='game',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 11, 19, 12, 46, 665487, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 11, 19, 12, 46, 665932, tzinfo=utc), verbose_name='date published'),
        ),
    ]