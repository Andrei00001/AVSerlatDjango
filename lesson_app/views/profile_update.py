from django.shortcuts import render, redirect
from django.views import View

from lesson_app.forms.update_profile import UpdateProfileForm, UpdateProfileAvaForm


class UserUpd(View):

    def get(self, request):
        user_form = UpdateProfileForm(instance=request.user)
        photo_form = UpdateProfileAvaForm(instance=request.user.profile)
        context = {"title": "Добавить пост", "form": user_form, "photo_form": photo_form}
        return render(request, "update_profile.html", context)

    def post(self, request):
        user_form = UpdateProfileForm(data=request.POST, instance=request.user)
        photo_form = UpdateProfileAvaForm(files=request.FILES, data=request.POST, instance=request.user.profile)
        if user_form.is_valid() and photo_form.is_valid():
            user_form.save()
            photo_form.save()
            return redirect("profile")
        context = {
            "title": "Добавить пост",
            "user_form": user_form,
            "pfoto_form": photo_form
        }
        return render(request, "update_profile.html", context)
