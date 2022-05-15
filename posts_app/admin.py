from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe

from posts_app.models import ImagePost, Post


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