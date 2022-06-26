from django import forms

from chat_app.models import ChatGroupsName


class GroupNameForm(forms.ModelForm):
    class Meta:
        model = ChatGroupsName
        fields = ["title", "image"]

