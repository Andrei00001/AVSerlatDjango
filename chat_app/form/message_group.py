from django import forms

from chat_app.models import ChatInGroups


class MassageGroupForm(forms.ModelForm):
    image = forms.ImageField(label='Выберите фото',
                             required=False,
                             widget=forms.FileInput(attrs={'multiple': 'multiple'})
                             )

    class Meta:
        model = ChatInGroups
        fields = ["text", "image"]
        widgets = {
            "text": forms.TextInput(attrs={"cols": 100, "rows": 15}),

        }
