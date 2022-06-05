from lib2to3.fixes.fix_input import context

from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from comments_app.models import Comments
from posts_app.models import Post, ImagePost
from profile_app.models import Profile
from user_app.models import User, Friends, Subscriptions


class Profile_user(View):
    def get(self, request):
        if request.user.is_authenticated:
            user_ava = Profile.objects.filter(user=request.user)
            user_post = Post.objects.order_by('-id').filter(user=request.user)

            comment = Comments.objects.filter(user=request.user)
            post_image = ImagePost.objects.all()
            context = {"title": "Акк",
                       "users": user_ava,
                       "posts": user_post,
                       "comments": comment,
                       "post_image": post_image}
            return render(request, "profile_app/profile.html", context)
        return redirect("login")


class ProfilePeoples_user(View):
    def get(self, request, peopl):
        if request.user.is_authenticated:
            user = User.objects.get(username=peopl)
            posts = Post.objects.filter(user=user)
            friend = Friends.objects.filter(user=request.user).filter(friend=user)
            subscription = Subscriptions.objects.filter(user=request.user).filter(subscription=user)
            context = {"title": "Акк",
                       "add_friend": "Удалить из друзей",
                       "podpis": "Отписаться",
                       "users": user,
                       "posts": posts,
                       }
            if friend:
                if not subscription:
                    context = {"title": "Акк",
                               "add_friend": "Удалить из друзей",
                               "podpis": "Подписаться",
                               "users": user,
                               "posts": posts,
                               }

            else:
                context = {"title": "Акк",
                           "add_friend": "Добавить в друзья",
                           "podpis": "Подписаться",
                           "users": user,
                           "posts": posts,
                           }
            return render(request, "people_app/people_profile.html", context)
        return redirect("login")


class AddFriend(View):
    def get(self, request, peopl):
        if request.user.is_authenticated:
            friend = User.objects.get(username=peopl)
            Friends(user=request.user, friend=friend).save()
            Subscriptions(user=request.user, subscription=friend).save()
            Subscriptions(user=friend, subscription=request.user).save()
            return redirect(f'/profile/{peopl}')
        return redirect("login")


class AddSubscription(View):
    def get(self, request, peopl):
        if request.user.is_authenticated:
            subscription = User.objects.get(username=peopl)
            Subscriptions(user=request.user, subscription=subscription).save()
            return redirect(f'/profile/{peopl}')
        return redirect("login")


class DelSubscription(View):
    def get(self, request, peopl):
        if request.user.is_authenticated:
            subscription = User.objects.get(username=peopl)
            Subscriptions.objects.filter(user=request.user, subscription=subscription).delete()
            return redirect(f'/profile/{peopl}')
        return redirect("login")


class DelFriend(View):
    def get(self, request, peopl):
        if request.user.is_authenticated:
            friend = User.objects.get(username=peopl)
            Friends.objects.filter(user=request.user, friend=friend).delete()
            Subscriptions.objects.filter(user=request.user, subscription=friend).delete()
            return redirect(f'/profile/{peopl}')
        return redirect("login")
