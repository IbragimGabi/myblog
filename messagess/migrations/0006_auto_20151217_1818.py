# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import messagess.models


class Migration(migrations.Migration):

    dependencies = [
        ('messagess', '0005_auto_20151130_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='msgs',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 17, 18, 18, 36, 949000)),
        ),
        migrations.AlterField(
            model_name='msgs',
            name='file',
            field=models.FileField(upload_to=messagess.models.get_path, blank=True),
        ),
    ]
