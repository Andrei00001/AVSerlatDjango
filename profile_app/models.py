from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from user_app.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(null=True, blank=True)
    email_verify = models.BooleanField(default=False)

    def get_absolute_url(self):
        return "/profile"
