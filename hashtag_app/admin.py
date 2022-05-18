from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe

from hashtag_app.models import Tags, PostTags


@admin.register(Tags)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "tag")
    ordering = ("id", "tag")
    readonly_fields = ("id",)
    list_display_links = ("id",)


class TagsPostAdmin(admin.StackedInline):
    model = PostTags
    list_display = ("tag",)
    readonly_fields = ("tag",)
