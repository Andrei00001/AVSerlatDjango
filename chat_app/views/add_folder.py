from django.shortcuts import redirect, render
from django.views import View

from chat_app.form.add_folder import FolderNameForm
from chat_app.form.add_folder_group import FolderGroupsForm
from chat_app.models import ChatGroupsName


class AddFolder(View):
    def get(self, request):
        form = FolderNameForm()
        context = {"title": "Добавить папку групп", "form": form}
        return render(request, "chat_app/add_folder.html", context)

    def post(self, request):
        form = FolderNameForm(request.POST)
        if form.is_valid():
            name_folder_user = form.save(commit=False)
            name_folder_user.user = request.user
            name_folder_user.save()
            return redirect(f"/chats/")


class AddFolderGroups(View):
    def get(self, request, group):
        form = FolderGroupsForm()
        context = {"title": "Добавить папку групп", "form": form}
        return render(request, "chat_app/add_folder.html", context)

    def post(self, request, group):

        form = FolderGroupsForm(request.POST)
        f_group = ChatGroupsName.objects.get(pk=group)

        if form.is_valid():
            folder = form.save(commit=False)
            folder.group = f_group
            try:
                folder.save()
                return redirect(f"/chats/")
            except:
                return redirect(f"/chats/")
