# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0004_auto_20151124_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='avatar',
            field=models.ImageField(upload_to=b'C:/Django/myblog/myblog/media/avatars/', blank=True),
        ),
        migrations.AlterField(
            model_name='communitypost',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 24, 20, 21, 52, 463000)),
        ),
        migrations.AlterField(
            model_name='communitypost',
            name='file',
            field=models.FileField(upload_to=b'C:/Django/myblog/myblog/media/post/', blank=True),
        ),
    ]
