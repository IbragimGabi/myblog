# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20151125_1844'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='msgs',
            name='recipient',
        ),
        migrations.RemoveField(
            model_name='msgs',
            name='sender',
        ),
        migrations.AlterField(
            model_name='profile',
            name='date',
            field=models.DateField(default=datetime.date(2015, 11, 26)),
        ),
        migrations.DeleteModel(
            name='Msgs',
        ),
    ]
