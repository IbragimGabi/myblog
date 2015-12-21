# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('messagess', '0006_auto_20151217_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='msgs',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 17, 18, 20, 59, 156000)),
        ),
    ]
