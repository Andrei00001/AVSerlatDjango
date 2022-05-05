from django.contrib.auth import login
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from lesson_app.forms import RegisterUserForms
from lesson_app.views.profile import Profile_user


class RegisterUser(CreateView):
    form_class = RegisterUserForms
    template_name = "register.html"
    success_url = reverse_lazy("profile")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(Profile_user)