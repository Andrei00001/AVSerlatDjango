from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView

from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from lesson_app.forms import RegisterUserForms
from lesson_app.models import Post, Comments, Profile, Like


def main_page_one(request):
    posts = Post.objects.filter(is_public=True).order_by("-created_at", "-id").all()
    comment = Comments.objects.order_by("-created_at", "post_id_id").all()
    context = {"title": "дороу", "posts": posts, "comments": comment}
    return render(request, "main_page.html", context)


class RegisterUser(CreateView):
    form_class = RegisterUserForms
    template_name = "register.html"
    success_url = reverse_lazy("profile")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(profile_user)


def profile_user(request):
    person = User.objects.order_by("id").all()
    user_ava = Profile.objects.order_by("id").all()
    user_post = Post.objects.order_by("id").all()
    comment = Comments.objects.order_by("id").all()
    like = Like.objects.order_by("id").all()
    context = {"title": "Акк", "person": person, "users": user_ava, "posts": user_post, "comments": comment,
               "likes": like}
    return render(request, "profile.html", context)


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = "login.html"

    def get_success_url(self):
        return reverse_lazy('profile')


def logout_user(request):
    logout(request)
    return redirect("login")
