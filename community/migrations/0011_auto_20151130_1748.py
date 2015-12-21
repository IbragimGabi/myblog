# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0010_auto_20151128_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='avatar',
            field=models.ImageField(upload_to=b'C:\\Django\\myblog\\media/avatars/', blank=True),
        ),
        migrations.AlterField(
            model_name='communitycomment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 30, 17, 48, 31, 52000)),
        ),
        migrations.AlterField(
            model_name='communitycomment',
            name='file',
            field=models.FileField(upload_to=b'C:\\Django\\myblog\\media/comment/', blank=True),
        ),
        migrations.AlterField(
            model_name='communitypost',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 30, 17, 48, 31, 51000)),
        ),
        migrations.AlterField(
            model_name='communitypost',
            name='file',
            field=models.FileField(upload_to=b'C:\\Django\\myblog\\media/post/', blank=True),
        ),
    ]
