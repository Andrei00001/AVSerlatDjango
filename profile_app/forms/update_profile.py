from django import forms

from profile_app.models import User, Profile


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = User
        template_name = "update_profile.html"
        fields = ["last_name", "first_name", "email"]


class UpdateProfileAvaForm(forms.ModelForm):
    class Meta:
        model = Profile
        template_name = "update_profile.html"
        fields = ["image", "id"]
