from django.db.models import Q, Count
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from chat_app.form.massage import MassageForm
from chat_app.models import Chat, ChatGroupsName, FolderChatGroups, FolderGroups


class Chats(View):
    def get(self, request):
        folders = FolderChatGroups.objects.filter(user=request.user).all()
        groups = ChatGroupsName.objects.filter(Q(group_user__user=request.user)).exclude(
            folder_group__folder__in=folders)

        ddd = {}
        group = FolderGroups.objects.filter(folder__in=folders)
        for folder in folders:
            ss = set()
            for g in group:
                if g.folder == folder:
                    ss.add(g)
            ddd[folder] = ss

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

        context = {"title": "дороу", "chats": peoples, "groups": groups, "folders": folders, "ddd": ddd}

        return render(request, "chat_app/chats.html", context)
