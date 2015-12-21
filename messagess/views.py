import datetime
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render
from blogs.models import Subscription
from community.models import CommunityUser
from messagess.models import Msgs
from users.models import Profile, Friends, Blacklist


@login_required(login_url="/login")
def mail(request):
    profile = Profile.objects.get(user=request.user)
    subs = Subscription.objects.filter(user=profile)
    fr1 = Friends.objects.filter(friend1=profile)
    fr2 = Friends.objects.filter(friend2=profile)
    ban = Blacklist.objects.filter(banner=profile)
    comm = CommunityUser.objects.filter(user=profile)
    return render(request, "messagess/mail.html", {"profile": profile, "subs": subs, "fr1": fr1, "fr2": fr2, "ban": ban, "comm": comm })

@login_required(login_url="/login")
def chat(request, user_id):
    if request.method=="POST":
        profile = Profile.objects.get(user=request.user)
        rcp = Profile.objects.get(id=user_id)
        m = Msgs(text=request.POST["text"],
                 date=datetime.datetime.now(),
                 sender=profile,
                 recipient=rcp,
                 file=request.FILES.get("img",None)
                 )
        m.save()
        q1 = Q(sender=profile)
        q2 = Q(recipient=rcp)
        q3 = Q(sender=rcp)
        q4 = Q(recipient=profile)
        msgs = Msgs.objects.filter((q1&q2)|(q3&q4))
        msgs = msgs.order_by("-date")
        subs = Subscription.objects.filter(user=profile)
        fr1 = Friends.objects.filter(friend1=profile)
        fr2 = Friends.objects.filter(friend2=profile)
        ban = Blacklist.objects.filter(banner=profile)
        comm = CommunityUser.objects.filter(user=profile)
        return render(request, "messagess/chat.html", {"msgs": msgs, "rcp": rcp, "profile": profile, "subs": subs, "fr1": fr1, "fr2": fr2, "ban": ban, "comm": comm })
    else:
        profile = Profile.objects.get(user=request.user)
        rcp = Profile.objects.get(id=user_id)
        q1 = Q(sender=profile)
        q2 = Q(recipient=rcp)
        q3 = Q(sender=rcp)
        q4 = Q(recipient=profile)
        msgs = Msgs.objects.filter((q1&q2)|(q3&q4))
        msgs = msgs.order_by("-date")
        subs = Subscription.objects.filter(user=profile)
        fr1 = Friends.objects.filter(friend1=profile)
        fr2 = Friends.objects.filter(friend2=profile)
        ban = Blacklist.objects.filter(banner=profile)
        comm = CommunityUser.objects.filter(user=profile)
        return render(request, "messagess/chat.html", {"msgs": msgs, "rcp": rcp, "profile": profile, "subs": subs, "fr1": fr1, "fr2": fr2, "ban": ban, "comm": comm })