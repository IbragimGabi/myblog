# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0011_auto_20151130_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communitycomment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 30, 19, 47, 12, 375000)),
        ),
        migrations.AlterField(
            model_name='communitypost',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 30, 19, 47, 12, 373000)),
        ),
    ]
