from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Meta:
        db_table = 'auth_user'

    def get_absolute_url(self):
        return "/profile"


class Post(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=128, unique=False, blank=False, null=False, verbose_name="Заголовок")
    text = models.TextField(blank=False, null=False, verbose_name="Текст поста")
    is_public = models.BooleanField(default=True, verbose_name="К общему обозрению")
    image = models.ImageField(null=True, blank=True, verbose_name="Фото поста")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} -- {self.title}  я вытянул ID {self.id}"

    def get_absolute_url(self):
        return "/profile"


class Comments(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField(blank=False, null=False)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)

    def get_absolute_url(self):
        return "/profile"
