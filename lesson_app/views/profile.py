from django.shortcuts import render
from django.views import View

from lesson_app.models import Profile, Post, Comments, Like


class Profile_user(View):
    def get(self, request):

        user_ava = Profile.objects.order_by("id").all()
        user_post = Post.objects.all()
        comment = Comments.objects.all()
        like = Like.objects.order_by("id").all()
        context = {"title": "Акк", "users": user_ava, "posts": user_post, "comments": comment,
                   "likes": like}
        return render(request, "profile.html", context)