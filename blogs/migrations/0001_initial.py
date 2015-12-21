# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20151123_1740'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('info', models.CharField(max_length=1000)),
                ('status', models.BooleanField()),
                ('user', models.ForeignKey(related_name='blog_author', to='users.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('text', models.CharField(max_length=5000)),
                ('file', models.FileField(upload_to=b'C:/Django/myblog/myblog/media/comment/')),
                ('post', models.ForeignKey(related_name='comment_post', to='blogs.Blog')),
                ('user', models.ForeignKey(related_name='comment_author', to='users.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('text', models.CharField(max_length=10000)),
                ('annotation', models.CharField(max_length=1000)),
                ('file', models.FileField(upload_to=b'C:/Django/myblog/myblog/media/post/')),
                ('blog', models.ForeignKey(related_name='post_blog', to='blogs.Blog')),
                ('user', models.ForeignKey(related_name='post_author', to='users.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('blog', models.ForeignKey(related_name='sub_blog', to='blogs.Blog')),
                ('user', models.ForeignKey(related_name='sub_user', to='users.Profile')),
            ],
        ),
    ]
