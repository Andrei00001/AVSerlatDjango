from django.views.generic import UpdateView

from profile_app.models import Profile


class UpdateProfileAva(UpdateView):
    model = Profile
    template_name = "profile_app/update_profile.html"
    fields = ["image", ]
