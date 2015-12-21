from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from blogs.models import Subscription
from community.models import CommunityUser, Community, CommunityPost
from users.forms import EditForm
from users.models import Profile, Friends, Blacklist


@login_required(login_url="/login")
def community(request, comm_id):
    thcomm = Community.objects.get(id=comm_id)
    print thcomm.name
    posts = CommunityPost.objects.filter(comm=thcomm)
    profile = Profile.objects.get(user=request.user)
    subs = Subscription.objects.filter(user=profile)
    fr1 = Friends.objects.filter(friend1=profile)
    fr2 = Friends.objects.filter(friend2=profile)
    ban = Blacklist.objects.filter(banner=profile)
    comm = CommunityUser.objects.filter(user=profile)
    return render(request, "community/community.html", {"subs": subs,
                                                        "thcomm": thcomm,
                                                        "fr1": fr1,
                                                        "fr2": fr2,
                                                        "ban": ban,
                                                        "comm": comm,
                                                        "posts": posts})