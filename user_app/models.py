from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    class Meta:
        db_table = 'auth_user'

    def get_absolute_url(self):
        return "/profile"

