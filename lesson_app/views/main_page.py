from django.shortcuts import render, redirect
from django.views import View

from lesson_app.forms.add_comments_main_page_form import AddCommentsForm
from lesson_app.models import Post, Comments


class Main_page(View):
    def get(self, request):
        posts = Post.objects.filter(is_public=True).order_by("-created_at", "-id").all()
        comment = Comments.objects.order_by("created_at").all()
        form = AddCommentsForm()
        context = {"title": "дороу", "posts": posts, "comments": comment, "form": form}
        return render(request, "main_page.html", context)

    def post(self, request):
        new_request = request.POST.copy()
        new_request['user'] = request.user.id
        new_request['post_id'] = new_request['post.id']

        form = AddCommentsForm(new_request, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("main_page")
        print(form.errors)
        context = {
            "title": "Добавить пост",
            "form": form
        }
        return render(request, "main_page.html", context)
