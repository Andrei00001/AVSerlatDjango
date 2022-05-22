from django.contrib import admin

from menu_app.models import Menu, ClassMenu


class MenuAdmin(admin.StackedInline):
    model = Menu
    list_display = ("id", "title", "url")


@admin.register(ClassMenu)
class ClassMenuAdmin(admin.ModelAdmin):
    inlines = (
        MenuAdmin,
    )
    list_display = ("id", "title")

#
# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     inlines = (
#         PostImageAdmin,
#         TagsPostAdmin,
#
#     )
#     list_display = ("id", "created_at", "title", "text")
#     ordering = ("-created_at", "-id")
#     readonly_fields = ("created_at", "user")
#     list_display_links = ("id",)
