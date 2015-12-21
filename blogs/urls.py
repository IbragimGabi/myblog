from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^(?P<blog_id>\d+)/get_subs', 'blogs.views.get_subs'),
    url(r'^(?P<blog_id>\d+)/new', 'blogs.views.newpost',name="newP"),
    url(r'^(?P<blog_id>\d+)/delete', 'blogs.views.deleteblog', name="deleteB"),
    url(r'^(?P<blog_id>\d+)/post/(?P<post_id>\d+)/add', 'blogs.views.comment'),
    url(r'^(?P<blog_id>\d+)/post/(?P<post_id>\d+)', 'blogs.views.post', name="post"),
    url(r'^my/', 'blogs.views.my', name="my"),
    url(r'^new/', 'blogs.views.newblog', name="newB"),
    url(r'^(?P<blog_id>\d+)/', 'blogs.views.blog'),
]