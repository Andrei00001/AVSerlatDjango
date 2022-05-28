from django.contrib import admin

# Register your models here.
from like_app.models import Like


@admin.register(Like)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "user_id", "post_id")