from django.shortcuts import render, redirect
from django.views import View

from chat_app.form.add_group import GroupNameForm
from chat_app.models import ChatGroups, ChatGroupsName


class AddGroup(View):
    def get(self, request):
        form = GroupNameForm()
        context = {"title": "Добавить группу", "form": form}
        return render(request, "chat_app/add_group.html", context)

    def post(self, request):
        form = GroupNameForm(request.POST, request.FILES)

        if form.is_valid():
            new = request.POST.copy()
            form.save()
            chat_name = ChatGroupsName.objects.get(name=new['name'])
            ChatGroups.objects.create(user=request.user, group=chat_name, owner=True)
            return redirect(f"/chats/")
