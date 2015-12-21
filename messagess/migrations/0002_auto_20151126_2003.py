# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('messagess', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='msgs',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 26, 20, 3, 4, 414000)),
        ),
        migrations.AlterModelTable(
            name='msgs',
            table='mail',
        ),
    ]
