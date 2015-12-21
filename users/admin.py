from django.contrib import admin
from users.models import Profile
from users.models import Friends
from users.models import Blacklist



admin.site.register(Profile)
admin.site.register(Friends)
admin.site.register(Blacklist)