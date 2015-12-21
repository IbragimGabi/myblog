# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import community.models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0012_auto_20151130_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='avatar',
            field=models.ImageField(upload_to=community.models.get_path1, blank=True),
        ),
        migrations.AlterField(
            model_name='communitycomment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 17, 18, 18, 36, 945000)),
        ),
        migrations.AlterField(
            model_name='communitycomment',
            name='file',
            field=models.FileField(upload_to=community.models.get_path3, blank=True),
        ),
        migrations.AlterField(
            model_name='communitypost',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 17, 18, 18, 36, 943000)),
        ),
        migrations.AlterField(
            model_name='communitypost',
            name='file',
            field=models.FileField(upload_to=community.models.get_path2, blank=True),
        ),
    ]
