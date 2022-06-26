from django import forms

from chat_app.models import FolderGroups


class FolderGroupsForm(forms.ModelForm):
    class Meta:
        model = FolderGroups
        fields = ["folder", ]
