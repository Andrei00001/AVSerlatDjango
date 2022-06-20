from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin as UserAdminBase

from comments_app.models import Comments

from profile_app.admin import ProfileInline
from user_app.models import User


@admin.register(Comments)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "created_at", "text_comment", "post_id_id")
    ordering = ("-created_at", "-id")
    readonly_fields = ("created_at",)
    list_display_links = ("post_id_id", "id")


@admin.register(User)
class AdminUser(UserAdminBase):
    inlines = (
        ProfileInline,
    )
    list_display = ("username", "last_name", "first_name", "email")
