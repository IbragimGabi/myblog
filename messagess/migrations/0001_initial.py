# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20151126_1910'),
    ]

    operations = [
        migrations.CreateModel(
            name='Msgs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(default=datetime.datetime(2015, 11, 26, 19, 12, 25, 631000))),
                ('text', models.TextField()),
                ('file', models.FileField(upload_to=b'C:/Django/myblog/myblog/media/msgs/', blank=True)),
                ('recipient', models.ForeignKey(related_name='msgs_receive', to='users.Profile')),
                ('sender', models.ForeignKey(related_name='msgs_sent', to='users.Profile')),
            ],
        ),
    ]
