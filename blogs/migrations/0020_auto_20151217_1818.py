# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import blogs.models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0019_auto_20151130_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 17, 18, 18, 36, 936000)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 17, 18, 18, 36, 939000)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='file',
            field=models.FileField(upload_to=blogs.models.get_path2, blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 17, 18, 18, 36, 937000)),
        ),
    ]
