from django.db import models

# Create your models here.
from posts_app.models import Post


class Tags(models.Model):
    tag = models.CharField(max_length=64, null=True, blank=True)

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return "/profile"


class PostTags(models.Model):
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="tag_post")
