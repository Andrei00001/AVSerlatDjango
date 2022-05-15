from django import forms

from posts_app.forms.add_post import AddPostForm


class AddImagePostForm(AddPostForm):
    image = forms.ImageField(label='Выберите фото',
                             required=False,
                             widget=forms.FileInput(attrs={'multiple': 'multiple'})
                             )

    class Meta(AddPostForm.Meta):
        fields = AddPostForm.Meta.fields + ["image", ]
