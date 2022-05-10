from django.shortcuts import render, redirect
from django.views import View

from lesson_app.forms.add_post import AddPostForm


class AddPost(View):
    def get(self, request):
        form = AddPostForm()
        context = {"title": "Добавить пост", "form": form}
        return render(request, "addpost.html", context)

    def post(self, request):
        new_request = request.POST.copy()
        new_request['user'] = request.user.id
        form = AddPostForm(new_request, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("profile")
        print(form.errors)
        context = {
            "title": "Добавить пост",
            "form": form
        }
        return render(request, "addpost.html", context)
