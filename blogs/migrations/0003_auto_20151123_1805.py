# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20151123_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 23, 18, 5, 57, 396000)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 23, 18, 5, 57, 399000)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 23, 18, 5, 57, 398000)),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(),
        ),
    ]
