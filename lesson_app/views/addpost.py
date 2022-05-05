from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from lesson_app.forms.addpost import AddPostForm
from lesson_app.models import Post, Comments


class AddPost(View):
    def get(self, request):
        form = AddPostForm()
        context = {"title": "Добавить пост", "form": form}
        return render(request, "addpost.html", context)

    def post(self, request):
        if request.method in ("POST", "PUT"):
            data = request.POST.copy()
            data['user'] = request.user.id

            form = AddPostForm(data, request.FILES)

            if form.is_valid():

                form.save()
                return redirect("profile")
            print(form.errors)
            context = {
                "title": "Добавить пост",
                "form": form
            }
            return render(request, "addpost.html", context)