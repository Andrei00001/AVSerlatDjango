from django import forms

from chat_app.models import FolderChatGroups


class FolderNameForm(forms.ModelForm):
    class Meta:
        model = FolderChatGroups
        fields = ["name", ]
        widgets = {
            "name": forms.TextInput(attrs={"cols": 100, "rows": 15}),

        }
