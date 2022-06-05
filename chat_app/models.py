import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models

from user_app.models import User


class Chat(models.Model):
    text = models.CharField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)
    sending_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sending_user")
    host_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="host_user")
