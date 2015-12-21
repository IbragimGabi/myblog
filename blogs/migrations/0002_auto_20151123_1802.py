# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 23, 18, 2, 26, 536000)),
        ),
        migrations.AddField(
            model_name='blog',
            name='subscriptions',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 23, 18, 2, 26, 540000)),
        ),
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 23, 18, 2, 26, 538000)),
        ),
    ]
