# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20151124_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='msgs',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 24, 12, 51, 19, 462000)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date',
            field=models.DateField(default=datetime.date(2015, 11, 24)),
        ),
    ]
