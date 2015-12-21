# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20151123_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(upload_to=b'C:/Django/myblog/myblog/media/avatars/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
