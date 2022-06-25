from django.db.models import Q, Count
from django.shortcuts import render, redirect
from django.views import View

from chat_app.form.massage import MassageForm
from chat_app.models import Chat, ChatGroupsName
from user_app.models import User


class Chats(View):
    def get(self, request):
        groups = ChatGroupsName.objects.all()
        chat = Chat.objects.filter(
            Q(sending_user=request.user)
            |
            Q(host_user=request.user)
        ).order_by('sending_user')

        peoples = set()

        for people in chat:

            if people.sending_user == request.user:
                peoples.add(people.host_user)
            else:
                peoples.add(people.sending_user)

        context = {"title": "дороу", "chats": peoples, "groups":groups}

        return render(request, "chat_app/chats.html", context)

    # def post(self, request, username):
    #     form = MassageForm(request.POST)
    #     files = request.FILES.getlist('image')
    #
    #     if form.is_valid():
    #         for i, file in enumerate(files):
    #             message = Chat(
    #                 sending_user=request.user,
    #                 host_user=User.objects.get(username=username),
    #                 text=form.cleaned_data['text'],
    #                 image=file
    #             )
    #             if i == 0:
    #                 message.save()
    #             else:
    #                 message.text = None
    #                 message.save()
    #         return redirect(f"/friends/chat/{username}")
    #     print(form.errors)
