from django.shortcuts import render, redirect
from django.views import View

from posts_app.models import Post
from profile_app.models import Profile
from user_app.models import User


class PeopleView(View):
    def get(self, request):
        people = Profile.objects.exclude(user=request.user).filter(email_verify=True)
        context = {"title": "Люди", "people": people}
        return render(request, "people_app/people.html", context)
