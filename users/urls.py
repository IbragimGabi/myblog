from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^my/', 'users.views.my', name="my"),
    url(r'^create/', 'users.views.create', name="create"),
    url(r'^edit/', 'users.views.edit', name="edit"),
    url(r'^(?P<user_id>\d+)/', 'users.views.user'),
]
