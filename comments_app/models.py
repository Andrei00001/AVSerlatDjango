from django.db import models

# Create your models here.

from django.db import models

from posts_app.models import Post
from user_app.models import User


class Comments(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    text_comment = models.TextField(blank=False, null=False)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post_user_comments")
