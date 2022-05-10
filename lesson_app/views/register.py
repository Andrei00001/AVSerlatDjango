from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView

from lesson_app.forms.register_user_forms import RegisterUserForms


class RegisterUser(CreateView):
    form_class = RegisterUserForms
    template_name = "register.html"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("profile")
