# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0008_auto_20151123_1852'),
        ('users', '0009_auto_20151123_1852'),
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('about', models.TextField(blank=True)),
                ('avatar', models.ImageField(upload_to=b'C:/Django/myblog/myblog/media/avatars/')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityPost',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('text', models.TextField()),
                ('annotation', models.CharField(max_length=1000)),
                ('file', models.FileField(upload_to=b'C:/Django/myblog/myblog/media/post/')),
                ('date', models.DateTimeField(default=datetime.datetime(2015, 11, 23, 18, 52, 2, 140000))),
                ('blog', models.ForeignKey(related_name='com_post_blog', to='blogs.Blog')),
                ('comm', models.ForeignKey(related_name='post_comm', to='community.Community')),
                ('user', models.ForeignKey(related_name='com_post_author', to='users.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.BooleanField()),
                ('community', models.ForeignKey(related_name='com_blog', to='community.Community')),
                ('user', models.ForeignKey(related_name='com_user', to='users.Profile')),
            ],
        ),
    ]
