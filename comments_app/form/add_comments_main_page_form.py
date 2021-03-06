from django import forms

from comments_app.models import Comments


class AddCommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ["text_comment", "post_id", "user"]
        widgets = {
            "text_comment": forms.TextInput(attrs={"cols": 60, "rows": 10}),
            "user": forms.HiddenInput(),
            "post_id": forms.HiddenInput()
        }
