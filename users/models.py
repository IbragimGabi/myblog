import os
from django.db import models
from django.contrib.auth.models import User
from myblog import settings
import datetime

GENDER = (
    ('F', 'Female'),
    ('M', 'Male')
)

def get_path(instance, filename):
    return os.path.join("avatar", filename)

class Profile(models.Model):
    class Meta:
        db_table = "profiles"

    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User)
    gender = models.CharField(max_length=1, choices=GENDER)
    about_me = models.TextField(blank=True)
    avatar = models.ImageField(upload_to=get_path)
    link = models.TextField(max_length=30)
    date = models.DateField(blank=True,default=datetime.date.today())

    def __unicode__(self):
        return self.user.username

class Friends(models.Model):
    friend1 = models.ForeignKey(Profile, related_name="friend1")
    friend2 = models.ForeignKey(Profile, related_name="friend2")

class Blacklist(models.Model):
    banner = models.ForeignKey(Profile, related_name="banner")
    banned = models.ForeignKey(Profile, related_name="banned")

