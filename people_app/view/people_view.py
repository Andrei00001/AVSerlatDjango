from django.shortcuts import render, redirect
from django.views import View

from posts_app.models import Post
from user_app.models import User


class PeopleView(View):
    def get(self, request):
        if request.user.is_authenticated:
            people = User.objects.exclude(username=request.user.username)
            context = {"title": "Люди", "people": people}
            return render(request, "people_app/people.html", context)
        return redirect("login")
