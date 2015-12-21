# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0016_auto_20151126_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 28, 13, 33, 7, 955000)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 28, 13, 33, 7, 958000)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(related_name='comment_post', to='blogs.Post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 28, 13, 33, 7, 956000)),
        ),
    ]
