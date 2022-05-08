from django.views.generic import UpdateView
from lesson_app.models import Post


class UpdatePostForm(UpdateView):
    model = Post
    template_name = "addpost.html"
    fields = ["title", "text", "is_public", "image"]



