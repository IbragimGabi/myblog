import os
from django.db import models
from users.models import Profile
from myblog import settings
import datetime
class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    user = models.ForeignKey(Profile, related_name="blog_author")
    info = models.CharField(max_length=1000,blank=True )
    status = models.BooleanField()
    date = models.DateTimeField(default=datetime.datetime.now())
    subscriptions = models.SmallIntegerField(default=0)

    def __unicode__(self):
        return self.name

def get_path1(instance, filename):
    return os.path.join("post", filename)

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    blog = models.ForeignKey(Blog, related_name="post_blog")
    user = models.ForeignKey(Profile, related_name="post_author")
    text = models.TextField()
    annotation = models.CharField(max_length=1000,blank=True)
    file = models.FileField(upload_to=get_path1,blank=True)
    date = models.DateTimeField(default=datetime.datetime.now())

    def __unicode__(self):
        return self.name

def get_path2(instance, filename):
    return os.path.join("comment", filename)

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, related_name="comment_post")
    user = models.ForeignKey(Profile, related_name="comment_author")
    text = models.TextField()
    file = models.FileField(upload_to=get_path2,blank=True)
    date = models.DateTimeField(default=datetime.datetime.now())

class Subscription(models.Model):
    user = models.ForeignKey(Profile, related_name="sub_user")
    blog = models.ForeignKey(Blog, related_name="sub_blog")

