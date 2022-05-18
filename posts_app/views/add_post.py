import re

from django.shortcuts import render, redirect
from django.views import View

from posts_app.models import Post, ImagePost
from posts_app.forms.add_image_post import AddImagePostForm


class AddPost(View):
    def get(self, request):
        form = AddImagePostForm()
        context = {"title": "Добавить пост", "form": form}
        return render(request, "posts_app/add_post.html", context)

    def post(self, request):
        form = AddImagePostForm(request.POST or None, request.FILES or None)
        files = request.FILES.getlist('image')
        if form.is_valid():
            user = request.user
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            is_public = form.cleaned_data['is_public']
            post_obj = Post.objects.create(user=user, title=title, text=text, is_public=is_public)
            for f in files:
                ImagePost.objects.create(post_image=post_obj, image=f)
            return redirect("profile")
        print(form.errors)
        context = {
            "title": "Добавить пост",
            "form": form
        }
        return render(request, "posts_app/add_post.html", context)
