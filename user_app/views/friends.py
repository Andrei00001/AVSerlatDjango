from django.shortcuts import render, redirect
from django.views import View

from user_app.models import Friends, Subscriptions


class Friends_user(View):
    def get(self, request):
        if request.user.is_authenticated:
            friends = Friends.objects.filter(user=request.user)
            v_friend = Friends.objects.filter(friend=request.user, confirmation=False)
            subscriptions = Subscriptions.objects.filter(user=request.user)
            context = {"title": "дороу", "friends": friends, "v_friend": v_friend, "subscriptions": subscriptions}
            return render(request, "user_app/friends.html", context)
        return redirect("login")
