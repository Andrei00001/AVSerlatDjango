from lesson_app.models import Post, ImagePost
from django import forms


class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "text", "is_public"]


