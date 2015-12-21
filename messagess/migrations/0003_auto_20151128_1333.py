# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('messagess', '0002_auto_20151126_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='msgs',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 28, 13, 33, 7, 968000)),
        ),
    ]
