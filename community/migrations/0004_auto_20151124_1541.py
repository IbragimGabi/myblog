# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0003_auto_20151124_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communitypost',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 24, 15, 41, 38, 822000)),
        ),
    ]
