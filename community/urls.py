from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^new/', 'community.views.create', name="new"),
    url(r'^(?P<comm_id>\d+)/', 'community.views.community'),
]
