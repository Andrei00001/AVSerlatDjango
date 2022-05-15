from django.contrib import admin

# Register your models here.


from django.utils.safestring import mark_safe
from django.contrib.auth.admin import UserAdmin as UserAdminBase
from profile_app.models import Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    list_display = ("user", "get_image")
    readonly_fields = ("user", "get_image")

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f"<a href={obj.image.url}>"
                             f"<img src={obj.image.url} width='50' height='50'>"
                             f"</a>")

    get_image.short_description = "Аватарка"
