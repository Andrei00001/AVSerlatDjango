from django.shortcuts import render
from django.views import View

from lesson_app.models import Profile, Post, Comments, Like, ImagePost


class Profile_user(View):
    def get(self, request):
        user_ava = Profile.objects.filter(user=request.user)
        user_post = Post.objects.order_by('-id').all()
        comment = Comments.objects.all()
        like = Like.objects.order_by("id").all()
        post_image = ImagePost.objects.all()
        context = {"title": "Акк",
                   "users": user_ava,
                   "posts": user_post,
                   "comments": comment,
                   "likes": like,
                   "post_image": post_image}
        return render(request, "profile.html", context)
