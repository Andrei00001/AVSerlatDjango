from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin as UserAdminBase
from django.contrib.auth.models import User

from comments_app.models import Comments
from posts_app.models import Like
from profile_app.admin import ProfileInline


@admin.register(Comments)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "created_at", "text_comment", "post_id_id")
    ordering = ("-created_at", "-id")
    readonly_fields = ("created_at",)
    list_display_links = ("post_id_id", "id")


@admin.register(Like)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "user_id", "post_id")


@admin.register(User)
class AdminUser(UserAdminBase):
    inlines = (
        ProfileInline,
    )
    list_display = ("username", "last_name", "first_name", "email")

# @admin.register(Profile)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ("user", "get_image")
#     readonly_fields = ("get_image",)
#
#     def get_image(self, obj):
#         if obj.image:
#             return mark_safe(f"<img src={obj.image.url} width='50' height='50' >")
#
#     get_image.short_description = "Аватарка"
