# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20151128_1333'),
        ('community', '0009_auto_20151126_2003'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommunityComment',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('text', models.TextField()),
                ('file', models.FileField(upload_to=b'C:/Django/myblog/myblog/media/comment/', blank=True)),
                ('date', models.DateTimeField(default=datetime.datetime(2015, 11, 28, 13, 33, 7, 964000))),
            ],
        ),
        migrations.RemoveField(
            model_name='communitypost',
            name='blog',
        ),
        migrations.AlterField(
            model_name='communitypost',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 28, 13, 33, 7, 962000)),
        ),
        migrations.AddField(
            model_name='communitycomment',
            name='post',
            field=models.ForeignKey(related_name='comment_comm', to='community.CommunityPost'),
        ),
        migrations.AddField(
            model_name='communitycomment',
            name='user',
            field=models.ForeignKey(related_name='comment_author_comm', to='users.Profile'),
        ),
    ]
