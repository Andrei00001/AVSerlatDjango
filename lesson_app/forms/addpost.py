from django import forms

from lesson_app.models import Post


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "text", "is_public", "image", "user"]
        widgets = {'user': forms.HiddenInput()}
