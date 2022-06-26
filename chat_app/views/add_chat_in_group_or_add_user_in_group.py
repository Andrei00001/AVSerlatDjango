from django.shortcuts import render, redirect
from django.views import View

from chat_app.form.message_group import MassageGroupForm
from chat_app.models import ChatGroups, ChatGroupsName, ChatInGroups


class AddUserInGroupOrAddUser(View):
    def get(self, request, chat):
        group_chat = ChatGroupsName.objects.get(pk=chat)
        ChatGroups.objects.create(user=request.user, group=group_chat)
        return redirect(f"/chats/{chat}")


class AddChatInGroupOrAddUser(View):
    def get(self, request, chat):
        group_chat = ChatGroupsName.objects.get(pk=chat)
        text_chat = ChatInGroups.objects.filter(group=group_chat)
        form = MassageGroupForm()
        try:
            ChatGroups.objects.get(user=request.user, group=group_chat)
            context = {"title": "Добавить группу", "add": True, "text": text_chat, "form": form,"group": chat}
        except:
            context = {"title": "Добавить группу", "add": False, "text": text_chat, "group": chat}
        return render(request, "chat_app/chat_group.html", context)

    def post(self, request, chat):
        form = MassageGroupForm(request.POST)
        files = request.FILES.getlist('image')
        group_chat = ChatGroupsName.objects.get(pk=chat)
        if form.is_valid():
            message = ChatInGroups(
                user=request.user,
                group=group_chat,
                text=form.cleaned_data['text']
            )
            if files:
                for i, file in enumerate(files):
                    message = ChatInGroups(
                        user=request.user,
                        group=group_chat,
                        text=form.cleaned_data['text'],
                        image=file,
                    )
                    if i == 0:
                        message.save()
                    else:
                        message.text = None
                        message.save()
            else:
                message.save()
        return redirect(f"/chats/{chat}")
