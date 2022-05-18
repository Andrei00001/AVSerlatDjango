from django.db.models import Avg
from django.shortcuts import render, redirect
from django.views import View

from comments_app.models import Comments
from hashtag_app.models import PostTags, Tags

from posts_app.models import Post, ImagePost
from comments_app.form.add_comments_main_page_form import AddCommentsForm


class PostTag(View):
    def get(self, request, tag):
        tag = Tags.objects.get(tag=tag)
        posts_tag = PostTags.objects.filter(tag=tag).order_by("-id").all()
        posts = (Post.objects.filter(is_public=True).order_by("-id").all())
        image_post = ImagePost.objects.all()
        comment = Comments.objects.order_by("created_at").all()
        form = AddCommentsForm()
        context = {"title": "Галерея #тэгов", "posts": posts, "tags": posts_tag, "comments": comment, "form": form,
                   "image_post": image_post,
                   }
        return render(request, "hashtag/hashtag_page.html", context)

    def post(self, request, tag):
        new_request = request.POST.copy()
        new_request['user'] = request.user.id
        new_request['post_id'] = new_request['post.id']

        print(new_request)
        form = AddCommentsForm(new_request, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(f"/tag_post/%23{tag[1:]}/")
        print(form.errors)
        context = {
            "title": "Добавить пост",
            "form": form
        }
        return render(request, "hashtag/hashtag_page.html", context)
