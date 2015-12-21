# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0012_auto_20151124_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 25, 18, 44, 8, 167000)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 25, 18, 44, 8, 170000)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 25, 18, 44, 8, 168000)),
        ),
    ]
