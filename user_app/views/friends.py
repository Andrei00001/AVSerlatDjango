from django.shortcuts import render, redirect
from django.views import View

from comments_app.form.add_comments_main_page_form import AddCommentsForm
from user_app.models import Friends


class Friends_user(View):
    def get(self, request):
        if request.user.is_authenticated:
            friends = Friends.objects.filter(user=request.user)
            context = {"title": "дороу", "friends": friends}
            return render(request, "user_app/friends.html", context)
        return redirect("login")

    def post(self, request):
        if request.user.is_authenticated:
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
            return render(request, "./main_page.html", context)

        return redirect("login")
