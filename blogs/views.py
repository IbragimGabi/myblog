from django.contrib.sessions import serializers
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from blogs.models import Blog, Comment
from django.db.models import F, Q
from datetime import datetime, date
from users.forms import LoginForm
from users.forms import EditForm
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from users.models import Profile
from blogs.models import Blog
from blogs.models import Subscription
from blogs.models import Post
from users.models import Friends
from users.models import Blacklist
from community.models import CommunityUser
from django.contrib.auth import get_user_model

@login_required(login_url="/login")
def my(request):
    profile = Profile.objects.get(user=request.user)
    blogs = Blog.objects.filter(user=profile)
    subs = Subscription.objects.filter(user=profile)
    fr1 = Friends.objects.filter(friend1=profile)
    fr2 = Friends.objects.filter(friend2=profile)
    ban = Blacklist.objects.filter(banner=profile)
    comm = CommunityUser.objects.filter(user=profile)
    return render(request, "blogs/my.html", {"profile": profile, "blogs": blogs, "subs": subs, "fr1": fr1, "fr2": fr2, "ban": ban, "comm": comm })

@login_required(login_url="/login")
def blog(request, blog_id):
    blog=Blog.objects.get(id=blog_id)
    #if blog.status==False and :
    posts=Post.objects.filter(blog=blog)
    profile = Profile.objects.get(user=request.user)
    subs = Subscription.objects.filter(user=profile)
    fr1 = Friends.objects.filter(friend1=profile)
    fr2 = Friends.objects.filter(friend2=profile)
    ban = Blacklist.objects.filter(banner=profile)
    comm = CommunityUser.objects.filter(user=profile)
    return render(request, "blogs/blog.html", {"subs": subs, "profile": profile, "blog": blog, "posts": posts, "fr1": fr1, "fr2": fr2, "ban": ban, "comm": comm })

@login_required(login_url="/login")
def post(request, post_id, blog_id):
    post = Post.objects.get(id=post_id)
    blog = Blog.objects.get(id=post.blog.id)
    comments = Comment.objects.filter(post=post)
    comments = comments.order_by("-date")
    profile = Profile.objects.get(user=request.user)
    subs = Subscription.objects.filter(user=profile)
    fr1 = Friends.objects.filter(friend1=profile)
    fr2 = Friends.objects.filter(friend2=profile)
    ban = Blacklist.objects.filter(banner=profile)
    comm = CommunityUser.objects.filter(user=profile)
    return render(request, "blogs/post.html", {"comments": comments, "subs": subs, "profile": profile, "blog": blog, "post": post, "fr1": fr1, "fr2": fr2, "ban": ban, "comm": comm })

@login_required(login_url="/login")
def comment(request, blog_id, post_id):
    profile = Profile.objects.get(user=request.user)
    post = Post.objects.get(id=post_id)
    if request.method=="POST":
        c = Comment(post=post,
                    user=profile,
                    text=request.POST.get("text"),
                    file=request.FILES.get("image")
                 )
        c.save()
        return HttpResponseRedirect(reverse("blog:post",kwargs={'post_id' : post_id, 'blog_id' : blog_id}))
    else:
       return HttpResponseRedirect(reverse("blog:post",kwargs={'post_id' : post_id, 'blog_id' : blog_id}))


@login_required(login_url="/login")
def newblog(request):
    profile = Profile.objects.get(user=request.user)
    if request.method=="POST":
        b = Blog(name=request.POST["name"],
                 user=profile,
                 info=request.POST["info"],
                 status=request.POST["status"],
                 date=datetime.now(),
                 )
        b.save()
        subs = Subscription.objects.filter(user=profile)
        fr1 = Friends.objects.filter(friend1=profile)
        fr2 = Friends.objects.filter(friend2=profile)
        ban = Blacklist.objects.filter(banner=profile)
        comm = CommunityUser.objects.filter(user=profile)
        return HttpResponseRedirect(reverse("blog:my"))
    else:
        subs = Subscription.objects.filter(user=profile)
        fr1 = Friends.objects.filter(friend1=profile)
        fr2 = Friends.objects.filter(friend2=profile)
        ban = Blacklist.objects.filter(banner=profile)
        comm = CommunityUser.objects.filter(user=profile)
        return render(request, "blogs/newblog.html", {"subs": subs, "profile": profile, "blog": blog, "post": post, "fr1": fr1, "fr2": fr2, "ban": ban, "comm": comm })

@login_required(login_url="/login")
def newpost(request, blog_id):
    profile = Profile.objects.get(user=request.user)
    blog = Blog.objects.get(id=blog_id)
    if request.method=="POST":
        p = Post(name=request.POST["name"],
                 user=profile,
                 blog=blog,
                 annotation=request.POST["annotation"],
                 text=request.POST["text"],
                 #file=request.FILES["image"],
                 date=datetime.now(),
                 )
        p.save()
        subs = Subscription.objects.filter(user=profile)
        fr1 = Friends.objects.filter(friend1=profile)
        fr2 = Friends.objects.filter(friend2=profile)
        ban = Blacklist.objects.filter(banner=profile)
        comm = CommunityUser.objects.filter(user=profile)
        return HttpResponseRedirect(reverse("blog:my"))
    else:
        subs = Subscription.objects.filter(user=profile)
        fr1 = Friends.objects.filter(friend1=profile)
        fr2 = Friends.objects.filter(friend2=profile)
        ban = Blacklist.objects.filter(banner=profile)
        comm = CommunityUser.objects.filter(user=profile)
        return render(request, "blogs/newpost.html", {"subs": subs, "profile": profile, "blog": blog, "post": post, "fr1": fr1, "fr2": fr2, "ban": ban, "comm": comm })


@login_required(login_url="/login")
def deleteblog(request, blog_id):
    b = Blog.objects.get(id=blog_id)
    profile = Profile.objects.get(user=request.user)
    subs = Subscription.objects.filter(user=profile)
    fr1 = Friends.objects.filter(friend1=profile)
    fr2 = Friends.objects.filter(friend2=profile)
    ban = Blacklist.objects.filter(banner=profile)
    comm = CommunityUser.objects.filter(user=profile)
    return HttpResponseRedirect(reverse("blog:my"))


@login_required(login_url="/login")
def get_subs(request, blog_id):
    b=Blog.objects.get(id=blog_id)
    subs=Subscription.objects.filter(blog=b)
    result = ", ".join(s.user.user.username for s in subs)
    return HttpResponse(result)