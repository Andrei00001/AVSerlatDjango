from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Meta:
        db_table = 'auth_user'

    def get_absolute_url(self):
        return "/profile"


class Friends(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name="friend")
    confirmation = models.BooleanField(default=True)


class Subscriptions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subscription = models.ForeignKey(User, on_delete=models.CASCADE, related_name="subscription")

