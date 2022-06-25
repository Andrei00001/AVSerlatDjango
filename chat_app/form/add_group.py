from django import forms

from chat_app.models import ChatGroupsName


class GroupNameForm(forms.ModelForm):
    class Meta:
        model = ChatGroupsName
        fields = ["name", "image"]
        widgets = {
            "text": forms.TextInput(attrs={"cols": 100, "rows": 15}),

        }
