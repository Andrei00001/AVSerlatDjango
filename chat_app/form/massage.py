from django import forms

from chat_app.models import Chat


class MassageForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ["text", "sending_user", "host_user"]
        widgets = {
            "text": forms.TextInput(attrs={"cols": 100, "rows": 15}),
            "sending_user": forms.HiddenInput(),
            "host_user": forms.HiddenInput(),

        }
