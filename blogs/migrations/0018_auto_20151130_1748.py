# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0017_auto_20151128_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 30, 17, 48, 31, 43000)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 30, 17, 48, 31, 46000)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='file',
            field=models.FileField(upload_to=b'C:\\Django\\myblog\\media/comment/', blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 30, 17, 48, 31, 45000)),
        ),
        migrations.AlterField(
            model_name='post',
            name='file',
            field=models.FileField(upload_to=b'C:\\Django\\myblog\\media/post/', blank=True),
        ),
    ]
