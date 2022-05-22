from django.shortcuts import redirect
from django.urls import reverse
from django.views import View

from comments_app.models import Comments


class DeleteCcomment(View):
    def get(self,request,pk):
        if request.user.is_authenticated:
            get_comment = Comments.objects.get(pk=pk)
            get_comment.delete()

            return redirect('profile')
        return redirect("login")