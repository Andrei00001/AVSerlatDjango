import os

from django.shortcuts import redirect
from django.urls import reverse
from django.views import View

from posts_app.models import Post


class DeletePpost(View):
    def get(self, request, pk):
        get_post = Post.objects.get(pk=pk)
        get_post.delete()
        return redirect(reverse('profile'))
