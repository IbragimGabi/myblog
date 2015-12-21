from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic import ListView
from blogs.models import Blog
from django.db.models import F, Q
from datetime import datetime, date
from users.forms import LoginForm, CreateUserForm
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
from myblog import settings

def create(request):
    if request.method == 'POST':
        if request.POST.get("password1")==request.POST.get("password2"):
            user = User.objects.create_user(username=request.POST.get("login"),
                                            password=request.POST.get("password1"))
            user.is_staff = False
            user.save()
            profile = Profile(user=user)
            profile.save()
            user = authenticate(
                username=request.POST.get("login"),
                password=request.POST.get('password1')
        )
            auth_login(request, user)
            return HttpResponseRedirect(reverse('users:edit'))
        else:
            return HttpResponseRedirect(reverse("index"))
    else:
        return HttpResponseRedirect(reverse("index"))

@login_required(login_url="/login")
def edit(request):
    if request.method == "POST":
        p = Profile.objects.get(user=request.user)
        #if p is None:
        #    p = Profile(user=request.user)
        p.date=request.POST["editdate"]
        form = EditForm(request.POST, request.FILES, instance=p)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("users:my"))
        else:
            return render(request, "users/edit.html", {"form": form})
    else:
        profile = Profile.objects.get(user=request.user)
        subs = Subscription.objects.filter(user=profile)
        fr1 = Friends.objects.filter(friend1=profile)
        fr2 = Friends.objects.filter(friend2=profile)
        ban = Blacklist.objects.filter(banner=profile)
        comm = CommunityUser.objects.filter(user=profile)
        if profile is None:
            form = EditForm()
        else:
            form = EditForm(instance=profile)
        return render(request, "users/edit.html", {"form": form,
                                                   "subs": subs,
                                                   "fr1": fr1,
                                                   "fr2": fr2,
                                                   "ban": ban,
                                                   "comm": comm})

@login_required(login_url="/login")
def my(request):
    profile = Profile.objects.get(user=request.user)
    blogs = Subscription.objects.filter(user=profile)
    fr1 = Friends.objects.filter(friend1=profile)
    fr2 = Friends.objects.filter(friend2=profile)
    ban = Blacklist.objects.filter(banner=profile)
    comm = CommunityUser.objects.filter(user=profile)
    return render(request, "users/my.html", {"profile": profile, "blogs": blogs, "fr1": fr1, "fr2": fr2, "ban": ban, "comm": comm })

@login_required(login_url="/login")
def user(request, user_id):
    profile = Profile.objects.get(user=request.user)
    #myblogs = Subscription.objects.filter(user=profile)
    subs = Subscription.objects.filter(user=profile)
    #user = Profile.objects.get(profile=user_id)
    users = Profile.objects.raw("select * from profiles where id="+user_id)
    blogs = Blog.objects.filter(user=users[0])
    fr1 = Friends.objects.filter(friend1=profile)
    fr2 = Friends.objects.filter(friend2=profile)
    ban = Blacklist.objects.filter(banner=profile)
    comm = CommunityUser.objects.filter(user=profile)
    return render(request, "users/user.html", {"subs": subs, "users": users, "profile": profile, "blogs": blogs, "fr1": fr1, "fr2": fr2, "ban": ban, "comm": comm })

class MyListView(ListView):
    q=Q(status=0)
    queryset = Blog.objects.filter(q)
    template_name = "users/index.html"

    def get_context_data(self, **kwargs):
        q=Q(status=0)
        blogs = Blog.objects.filter(q)
        posts = Post.objects.filter(blog=blogs)
        context = super(MyListView, self).get_context_data(**kwargs)
        context["posts"] = posts
        return context
# def index(request):
#         q=Q(status=0)
#         blogs = Blog.objects.filter(q)
#         posts = Post.objects.filter(blog=blogs)
#         return render(request, "users/index.html", {"posts": posts})

#@login_required(login_url="/login")
def login(request):
    if request.method=="POST":
        login=request.POST["login"]
        password=request.POST["password"]
        #form = LoginForm(request.POST)
        user = authenticate(
            username=request.POST["login"],
            password=request.POST['password']
        )
        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect(reverse("users:my"))
    else:
        return HttpResponseRedirect(reverse("index"))

@login_required(login_url="/login")
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect("/")