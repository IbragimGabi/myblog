from django.contrib import admin
from community.models import Community
from community.models import CommunityPost
from community.models import CommunityUser
from community.models import CommunityComment

admin.site.register(Community)
admin.site.register(CommunityUser)
admin.site.register(CommunityPost)
admin.site.register(CommunityComment)