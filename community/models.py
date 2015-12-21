import os
from django.db import models
from myblog import settings
from blogs.models import Blog
from users.models import Profile
import datetime

def get_path1(instance, filename):
    return os.path.join("avatar", filename)

class Community(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    about = models.TextField(blank=True)
    avatar = models.ImageField(upload_to=get_path1,blank=True )

    def __unicode__(self):
        return self.name

def get_path2(instance, filename):
    return os.path.join("commpost", filename)

class CommunityPost(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    user = models.ForeignKey(Profile, related_name="com_post_author")
    comm = models.ForeignKey(Community, related_name="post_comm")
    text = models.TextField()
    annotation = models.CharField(max_length=1000)
    file = models.FileField(upload_to=get_path2,blank=True)
    date = models.DateTimeField(default=datetime.datetime.now())

def get_path3(instance, filename):
    return os.path.join("commcomm", filename)


class CommunityComment(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(CommunityPost, related_name="comment_comm")
    user = models.ForeignKey(Profile, related_name="comment_author_comm")
    text = models.TextField()
    file = models.FileField(upload_to=get_path3, blank=True)
    date = models.DateTimeField(default=datetime.datetime.now())

class CommunityUser(models.Model):
    user = models.ForeignKey(Profile, related_name="com_user")
    community = models.ForeignKey(Community, related_name="com_blog")
    status = models.BooleanField()