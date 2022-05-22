from django.db.models import Avg, Count
from django.shortcuts import render, redirect
from django.views import View

from hashtag_app.models import Tags


class PostTagCloud(View):
    def get(self, request):

        tags = Tags.objects.annotate(count=Count("posttags")).order_by("-count")
        context = {"title": "Галерея #тэгов",
                   "tags": tags,
                   }
        return render(request, "hashtag/cloud.html", context)
