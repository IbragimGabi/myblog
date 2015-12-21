# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import blogs.models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0018_auto_20151130_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 30, 19, 47, 12, 365000)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 30, 19, 47, 12, 368000)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 30, 19, 47, 12, 366000)),
        ),
        migrations.AlterField(
            model_name='post',
            name='file',
            field=models.FileField(upload_to=blogs.models.get_path1, blank=True),
        ),
    ]
