import datetime
import os
from django.db import models
from myblog import settings
from users.models import Profile

def get_path(instance, filename):
    return os.path.join("mail", filename)

class Msgs(models.Model):
    class Meta:
        db_table="mail"

    sender = models.ForeignKey(Profile, related_name="msgs_sent")
    recipient = models.ForeignKey(Profile, related_name="msgs_receive")
    date = models.DateTimeField(default=datetime.datetime.now())
    text = models.TextField()
    file = models.FileField(upload_to=get_path, blank=True)
