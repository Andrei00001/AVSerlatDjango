from django.contrib import admin

from menu_app.models import Menu


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    model = Menu
    list_display = ("id","title", "url")


