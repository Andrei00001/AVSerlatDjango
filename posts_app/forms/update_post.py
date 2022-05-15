
from django import forms

from posts_app.models import Post


class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "text", "is_public"]


