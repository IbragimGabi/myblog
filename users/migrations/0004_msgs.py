# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20151123_1740'),
    ]

    operations = [
        migrations.CreateModel(
            name='Msgs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(default=datetime.datetime(2015, 11, 23, 18, 5, 57, 394000))),
                ('text', models.TextField()),
                ('file', models.FileField(upload_to=b'C:/Django/myblog/myblog/media/msgs/')),
                ('recipient', models.ForeignKey(related_name='msgs_receive', to='users.Profile')),
                ('sender', models.ForeignKey(related_name='msgs_sent', to='users.Profile')),
            ],
        ),
    ]
