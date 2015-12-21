# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20151128_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(upload_to=users.models.get_path),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date',
            field=models.DateField(default=datetime.date(2015, 11, 30)),
        ),
    ]
