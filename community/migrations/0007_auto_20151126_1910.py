# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0006_auto_20151125_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communitypost',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 26, 19, 10, 53, 134000)),
        ),
    ]
