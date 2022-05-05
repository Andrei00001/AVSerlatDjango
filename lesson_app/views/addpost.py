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
        # print(request.user.id)
        ss = User.objects.get(pk=request.user.id)
        print(ss)
        # , initial = {"user": request.user.id}
        if request.method in ("POST", "PUT"):
            data = request.POST.copy()
            data['user'] = ss

            form = AddPostForm(data, request.FILES)
        # form.instance.user = ss
            if form.is_valid():
                # instance = form.save(commit=False)
                # instance.user = request.user.id
                form.save()
                return redirect("profile")
            print(form.errors)
            context = {
                "title": "Добавить пост",
                "form": form
            }
            return render(request, "addpost.html", context)
