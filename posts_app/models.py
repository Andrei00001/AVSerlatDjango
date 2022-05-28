from django.db import models

# Create your models here.

from user_app.models import User


class Post(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=128, unique=False, blank=False, null=False, verbose_name="Заголовок")
    text = models.TextField(blank=False, null=False, verbose_name="Текст поста")
    is_public = models.BooleanField(default=True, verbose_name="К общему обозрению")
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class ImagePost(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    image = models.ImageField(null=True, blank=True, verbose_name="Фото поста")
    post_image = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_img")

