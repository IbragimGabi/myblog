# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20151124_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='msgs',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 24, 20, 21, 52, 451000)),
        ),
    ]
