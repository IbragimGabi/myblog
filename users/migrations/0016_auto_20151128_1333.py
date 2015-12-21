# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20151126_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date',
            field=models.DateField(default=datetime.date(2015, 11, 28)),
        ),
    ]
