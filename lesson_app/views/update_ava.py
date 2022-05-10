from django.views.generic import UpdateView

from lesson_app.models import Profile


class UpdateProfileAva(UpdateView):
    model = Profile
    template_name = "update_profile.html"
    fields = ["image", ]
