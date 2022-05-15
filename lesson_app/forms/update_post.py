from lesson_app.models import Post, ImagePost
from django import forms


class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "text", "is_public"]



class UpdateImagePostForm(forms.ModelForm):
    class Meta:
        model = ImagePost
        fields = ["id", "image", "post_image"]
        widgets = {
            "post_image": forms.HiddenInput(),
        }
