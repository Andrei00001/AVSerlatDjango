from django.db import models

# Create your models here.
from comments_app.models import Comments
from posts_app.models import Post
from user_app.models import User


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="like_user", unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("post", "user"),)


class LikeComments(models.Model):
    comment = models.ForeignKey(Comments, on_delete=models.CASCADE, related_name="like_comment_user")
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("comment", "user"),)
