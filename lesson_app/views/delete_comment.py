from django.shortcuts import redirect
from django.urls import reverse
from lesson_app.models import Comments


def delete_comment(request, pk):
    get_comment = Comments.objects.get(pk=pk)
    get_comment.delete()

    return redirect(reverse('profile'))
