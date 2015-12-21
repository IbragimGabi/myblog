"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from myblog import settings
from django.conf.urls.static import static
from users.views import MyListView

urlpatterns = [
    url(r'^$', MyListView.as_view(),name="index"),
    # url(r'^$', 'users.views.index', name="index"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/', include('users.urls', namespace="users")),
    url(r'^community/', include('community.urls', namespace="comm")),
    url(r'^blog/', include('blogs.urls', namespace="blog")),
    url(r'^login$', 'users.views.login', name="login"),
    url(r'^logout$', 'users.views.logout', name="logout"),
    url(r'^mail/', include('messagess.urls', namespace="msgs")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
