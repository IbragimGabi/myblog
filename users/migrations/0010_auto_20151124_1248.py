# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20151123_1852'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 24, 12, 48, 18, 832000)),
        ),
        migrations.AlterField(
            model_name='msgs',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 24, 12, 48, 18, 835000)),
        ),
    ]
