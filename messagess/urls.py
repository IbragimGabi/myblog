from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^(?P<user_id>\d+)', 'messagess.views.chat', name="chat"),
    url(r'^', 'messagess.views.mail', name="mail"),
]
