# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20151123_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='msgs',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 23, 18, 10, 51, 145000)),
        ),
    ]
