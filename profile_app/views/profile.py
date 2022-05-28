from lib2to3.fixes.fix_input import context

from django.shortcuts import render, redirect
from django.views import View

from comments_app.models import Comments
from posts_app.models import Post, ImagePost
from profile_app.models import Profile


class Profile_user(View):
    def get(self, request):
        if request.user.is_authenticated:
            user_ava = Profile.objects.filter(user=request.user)
            user_post = Post.objects.order_by('-id').filter(user=request.user)

            comment = Comments.objects.filter(user=request.user)
            post_image = ImagePost.objects.all()
            context = {"title": "Акк",
                       "users": user_ava,
                       "posts": user_post,
                       "comments": comment,
                       "post_image": post_image}
            return render(request, "profile_app/profile.html", context)
        return redirect("login")
