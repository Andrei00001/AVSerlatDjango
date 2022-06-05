from django.db.models import Avg, Count, Q
from django.shortcuts import render, redirect
from django.views import View

from chat_app.form.massage import MassageForm
from chat_app.models import Chat
from comments_app.models import Comments
from hashtag_app.models import Tags
from posts_app.models import Post, ImagePost
from comments_app.form.add_comments_main_page_form import AddCommentsForm
from user_app.models import Subscriptions, Friends, User


class Chat_page(View):
    def get(self, request, username):
        username = User.objects.get(username=username)
        chat = Chat.objects.filter(Q(sending_user=request.user) | Q(sending_user=username)).order_by("created_at")
        form = MassageForm()
        context = {"title": "дороу", "form": form, "chat": chat}
        return render(request, "chat_app/chat.html", context)

    def post(self, request, username):
        if request.user.is_authenticated:
            new_request = request.POST.copy()
            new_request['sending_user'] = request.user.id
            host_user = User.objects.get(username=username)
            new_request['host_user'] = host_user
            form = MassageForm(new_request, request.FILES)
            if form.is_valid():
                form.save()
                return redirect(f"/friends/chat/{username}")

        return redirect("login")
