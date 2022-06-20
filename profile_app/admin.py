from django.contrib import admin

# Register your models here.


from django.utils.safestring import mark_safe
from django.contrib.auth.admin import UserAdmin as UserAdminBase
from profile_app.models import Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    list_display = ("user", "get_image")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f"<a href={obj.image.url} target='_blank'>"
                             f"<img src={obj.image.url} width='100' height='100'>"
                             f"</a>")

    get_image.short_description = "Аватарка"

