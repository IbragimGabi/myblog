# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0008_auto_20151126_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communitypost',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 26, 20, 3, 4, 404000)),
        ),
    ]
