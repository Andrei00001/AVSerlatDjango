from django import forms
from django.views.generic import UpdateView

from lesson_app.models import User, Profile


class UpdateProfileForm(UpdateView):
    model = User
    template_name = "update_profile.html"
    fields = ["last_name", "first_name", "email"]


class UpdateProfileAvaForm(UpdateView):
    model = Profile
    template_name = "update_profile.html"
    fields = ["image", ]
