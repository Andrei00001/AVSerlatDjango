from django.shortcuts import render, redirect
from django.views import View


from profile_app.forms.update_profile import UpdateProfileForm, UpdateProfileAvaForm
from profile_app.models import Profile


class UserUpd(View):

    def get(self, request):
        if request.user.is_authenticated:
            user_form = UpdateProfileForm(instance=request.user)
            get_photo = Profile.objects.get(user=request.user)
            photo_form = UpdateProfileAvaForm( files=request.FILES, data=request.POST,instance=get_photo)
            context = {"title": "Добавить пост", "form": user_form, "photo_form": photo_form}
            return render(request, "profile_app/update_profile.html", context)
        return redirect("login")

    def post(self, request):
        user_form = UpdateProfileForm(data=request.POST, instance=request.user)
        get_photo = Profile.objects.get(user=request.user)
        photo_form = UpdateProfileAvaForm(files=request.FILES, data=request.POST, instance=get_photo)
        if user_form.is_valid() and photo_form.is_valid():
            user_form.save()
            photo_form.save()
            return redirect("profile")
        context = {
            "title": "Добавить пост",
            "user_form": user_form,
            "pfoto_form": photo_form
        }
        return render(request, "profile_app/update_profile.html", context)
