from django.contrib import admin
from blogs.models import Blog
from blogs.models import Post
from blogs.models import Comment
from blogs.models import Subscription


admin.site.register(Blog)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Subscription)