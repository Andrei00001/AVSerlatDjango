from django import forms

from chat_app.models import Chat


class MassageForm(forms.ModelForm):
    image = forms.ImageField(label='Выберите фото',
                             required=False,
                             widget=forms.FileInput(attrs={'multiple': 'multiple'})
                             )

    class Meta:
        model = Chat
        fields = ["text","image"]
        widgets = {
            "text": forms.TextInput(attrs={"cols": 100, "rows": 15}),

        }
