from django.db.models import Q
from django.shortcuts import render, redirect
from django.views import View

from chat_app.form.massage import MassageForm
from chat_app.models import Chat
from user_app.models import User


class Chat_page(View):
    def get(self, request, username):
        username = User.objects.get(username=username)
        chat = Chat.objects.filter(
            (Q(sending_user=request.user) & Q(host_user=username)) |
            (Q(sending_user=username) & Q(host_user=request.user))
        ).order_by("created_at")
        form = MassageForm()
        context = {"title": "дороу", "form": form, "chat": chat}
        return render(request, "chat_app/chat.html", context)

    def post(self, request, username):
        form = MassageForm(request.POST)
        files = request.FILES.getlist('image')

        if form.is_valid():
            for i, file in enumerate(files):
                message = Chat(
                    sending_user=request.user,
                    host_user=User.objects.get(username=username),
                    text=form.cleaned_data['text'],
                    image=file
                )
                if i == 0:
                    message.save()
                else:
                    message.text = None
                    message.save()
            return redirect(f"/friends/chat/{username}")
        print(form.errors)
