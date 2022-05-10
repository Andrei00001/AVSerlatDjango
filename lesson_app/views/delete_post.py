import os

from django.shortcuts import redirect
from django.urls import reverse
from django.views import View

from lesson_app.models import Post


class DeletePpost(View):
    def get(self, request, pk):
        get_post = Post.objects.get(pk=pk)
        if get_post.image:
            path = f".\media\{get_post.image}"
            os.remove(path)
        get_post.delete()

        return redirect(reverse('profile'))
