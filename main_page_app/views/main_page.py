from django.db.models import Avg, Count
from django.shortcuts import render, redirect
from django.views import View

from comments_app.models import Comments
from hashtag_app.models import Tags
from posts_app.models import Post, ImagePost
from comments_app.form.add_comments_main_page_form import AddCommentsForm
from user_app.models import Subscriptions, Friends


class Main_page(View):
    def get(self, request):
        # tags = Tags.objects.order_by('id').all()
        # count = dict()
        # for tag in tags:
        #     a = tag.posttags_set.count()
        #     count[tag] = a
        # sort_count = sorted(count.values())
        # sort_count = sort_count[-10:]
        # i = 0
        # tags = list()
        # while i < len(sort_count):
        #     for k, v in count.items():
        #         if v == sort_count[i]:
        #             tags.append(k)
        #             count.pop(k)
        #             break
        #     i += 1
        friends = Subscriptions.objects.filter(user=request.user)
        people = (Friends.objects.annotate(count=Count("user")).order_by("-count"))[:5]
        if friends:
            for friend in friends:
                post_friend = (Post.objects.filter(user=friend.subscription, is_public=True))
                tags = Tags.objects.annotate(count=Count("posttags")).order_by("-count")[:5]
                image_post = ImagePost.objects.all()
                comment = Comments.objects.order_by("created_at").all()
                form = AddCommentsForm()
                if post_friend:
                    context = {"title": "дороу", "post_friend": post_friend, "comments": comment, "form": form,
                               "image_post": image_post,
                               "tags": tags}
                else:
                    context = {"title": "дороу", "text": "Нету постов подпишись что их стало больше:",
                               "people": people}
        else:
            context = {"title": "дороу", "text": "Подпишись на них они самые популярные социопат чёртов:",
                       "people": people}
        return render(request, "main_page_app/main_page.html", context)

    def post(self, request):
        if request.user.is_authenticated:
            new_request = request.POST.copy()
            new_request['user'] = request.user.id
            new_request['post_id'] = new_request['post.id']
            form = AddCommentsForm(new_request, request.FILES)
            if form.is_valid():
                form.save()
                return redirect("main_page")
            print(form.errors)
            context = {
                "title": "Добавить пост",
                "form": form
            }
            return render(request, "./main_page.html", context)

        return redirect("login")
