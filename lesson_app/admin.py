from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin as UserAdminBase
from django.utils.safestring import mark_safe

from lesson_app.models import Post, Comments, Profile, Like, User, ImagePost


@admin.register(Comments)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "created_at", "text", "post_id_id")
    ordering = ("-created_at", "-id")
    readonly_fields = ("created_at",)
    list_display_links = ("post_id_id", "id")


@admin.register(Like)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "user_id", "post_id")


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


@admin.register(User)
class UserAdmin(UserAdminBase):
    inlines = (
        ProfileInline,
    )
    list_display = ("username", "last_name", "first_name", "email")


class PostImageAdmin(admin.StackedInline):
    model = ImagePost
    list_display = ("post_image", "get_image")
    readonly_fields = ("post_image", "get_image")

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f"<a href={obj.image.url}>"
                             f"<img src={obj.image.url} width='50' height='50'>"
                             f"</a>")

    get_image.short_description = "Фото к посту"


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = (
        PostImageAdmin,
    )
    list_display = ("id", "created_at", "title", "text")
    ordering = ("-created_at", "-id")
    readonly_fields = ("created_at", "user")
    list_display_links = ("id",)

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
