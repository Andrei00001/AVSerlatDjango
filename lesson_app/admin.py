from django.contrib import admin

# Register your models here.
from lesson_app.models import Post, Comments, Profile, Like


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "created_at", "title", "text")
    ordering = ("-created_at", "-id")
    readonly_fields = ("created_at",)
    list_display_links = ("id",)



@admin.register(Comments)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "created_at", "text", "post_id_id")
    ordering = ("-created_at", "-id")
    readonly_fields = ("created_at",)
    list_display_links = ("post_id_id", "id")


@admin.register(Profile)
class PostAdmin(admin.ModelAdmin):
    list_display = ("user",)


@admin.register(Like)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "user_id", "post_id")
