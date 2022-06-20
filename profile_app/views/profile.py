from lib2to3.fixes.fix_input import context

from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from comments_app.models import Comments
from posts_app.models import Post, ImagePost
from profile_app.models import Profile
from user_app.models import User, Friends, Subscriptions


class Profile_user(View):
    def get(self, request):

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



class ProfilePeoples_user(View):
    def get(self, request, peopl):

            user = User.objects.get(Q(email=peopl) | Q(username=peopl))
            posts = Post.objects.filter(user=user)
            friend = Friends.objects.filter(Q(user=request.user) | Q(friend=request.user))
            subscription = Subscriptions.objects.filter(Q(user=request.user) | Q(subscription=request.user))
            context = {"title": "Акк",
                       "add_friend": "Добавить в друзья",
                       "podpis": "Подписаться",
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
                               "add_friend": "Удалить из друзей",
                               "podpis": "Отписаться",
                               "users": user,
                               "posts": posts,
                               }

            else:
                if subscription:
                    context = {"title": "Акк",
                               "add_friend": "Добавить в друзья",
                               "podpis": "Отписаться",
                               "users": user,
                               "posts": posts,
                               }

            return render(request, "people_app/people_profile.html", context)



class AddFriend(View):
    def get(self, request, peopl):

            friend = User.objects.get(email=peopl)
            Friends(user=request.user, friend=friend, confirmation=False).save()
            return redirect("friends")



class ConfirmationFriend(View):
    def get(self, request, peopl):

            friend = User.objects.get(username=peopl)
            a_friend = Friends.objects.get(friend=request.user, user=friend)
            a_friend.confirmation = True
            a_friend.save()
            subscriptions = Subscriptions.objects.get(Q(subscription=friend) | Q(user=friend))
            if not subscriptions:
                Subscriptions(user=request.user, subscription=friend).save()
            return redirect("friends")



class AddSubscription(View):
    def get(self, request, peopl):

            subscription = User.objects.get(email=peopl)
            Subscriptions(user=request.user, subscription=subscription).save()
            return redirect(f'/profile/{peopl}')



class DelSubscription(View):
    def get(self, request, peopl):

            subscription = User.objects.get(email=peopl)

            Subscriptions.objects.filter(
                Q(user=request.user, subscription=subscription)
                |
                Q(subscription=request.user, user=subscription)
            ).delete()

            return redirect(f'/profile/{peopl}')



class DelFriend(View):
    def get(self, request, peopl):

            friend = User.objects.get(Q(email=peopl) | Q(username=peopl))
            Friends.objects.filter(
                Q(user=request.user, friend=friend)
                |
                Q(user=friend, friend=request.user)
            ).delete()
            return redirect("friends")

