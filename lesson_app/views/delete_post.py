import os

from django.shortcuts import redirect
from django.urls import reverse
from lesson_app.models import Post


def delete_post(request,pk):
    get_post = Post.objects.get(pk=pk)
    path = f".\media\{get_post.image}"
    os.remove(path)
    get_post.delete()

    return redirect(reverse('profile'))




