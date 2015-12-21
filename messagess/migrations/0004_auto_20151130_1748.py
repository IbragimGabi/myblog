# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('messagess', '0003_auto_20151128_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='msgs',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 30, 17, 48, 31, 56000)),
        ),
        migrations.AlterField(
            model_name='msgs',
            name='file',
            field=models.FileField(upload_to=b'C:\\Django\\myblog\\media/msgs/', blank=True),
        ),
    ]
