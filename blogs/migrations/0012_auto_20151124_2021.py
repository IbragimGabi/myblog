# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0011_auto_20151124_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 24, 20, 21, 52, 454000)),
        ),
        migrations.AlterField(
            model_name='blog',
            name='info',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 24, 20, 21, 52, 457000)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='file',
            field=models.FileField(upload_to=b'C:/Django/myblog/myblog/media/comment/', blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='annotation',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 24, 20, 21, 52, 456000)),
        ),
        migrations.AlterField(
            model_name='post',
            name='file',
            field=models.FileField(upload_to=b'C:/Django/myblog/myblog/media/post/', blank=True),
        ),
    ]
