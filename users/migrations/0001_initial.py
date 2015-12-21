# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blacklist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gender', models.CharField(max_length=1, choices=[(b'F', b'Female'), (b'M', b'Male')])),
                ('about_me', models.TextField(blank=True)),
                ('avatar', models.ImageField(upload_to=b'/avatars')),
                ('link', models.TextField(max_length=30)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='friends',
            name='friend1',
            field=models.ForeignKey(related_name='friend1', to='users.Profile'),
        ),
        migrations.AddField(
            model_name='friends',
            name='friend2',
            field=models.ForeignKey(related_name='friend2', to='users.Profile'),
        ),
        migrations.AddField(
            model_name='blacklist',
            name='banned',
            field=models.ForeignKey(related_name='banned', to='users.Profile'),
        ),
        migrations.AddField(
            model_name='blacklist',
            name='banner',
            field=models.ForeignKey(related_name='banner', to='users.Profile'),
        ),
    ]
