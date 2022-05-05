from django.shortcuts import render
from django.views import View

from lesson_app.models import Post, Comments


class Main_page(View):
    def get(self, request):
        posts = Post.objects.filter(is_public=True).order_by("-created_at", "-id").all()
        comment = Comments.objects.order_by("-created_at", "post_id_id").all()
        context = {"title": "дороу", "posts": posts, "comments": comment}
        return render(request, "main_page.html", context)
