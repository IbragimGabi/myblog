# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_auto_20151130_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date',
            field=models.DateField(blank=True),
        ),
    ]
