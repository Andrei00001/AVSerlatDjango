import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models

from user_app.models import User


class Chat(models.Model):
    text = models.CharField(max_length=1024, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    sending_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sending_user")
    host_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="host_user")
    image = models.ImageField(null=True, blank=True, verbose_name="Фото чата")


class FolderChatGroups(models.Model):
    name = models.CharField(max_length=1024, null=False, blank=False, verbose_name="Имя папки", unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users_folder")


class ChatGroupsName(models.Model):
    title = models.CharField(max_length=1024, null=False, blank=False, verbose_name="Имя группы", unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=False, blank=False, verbose_name="Фото группы")


class FolderGroups(models.Model):
    folder = models.ForeignKey(FolderChatGroups, on_delete=models.CASCADE, related_name="group_folder")
    group = models.OneToOneField(ChatGroupsName, on_delete=models.CASCADE, related_name="folder_group")


class ChatGroups(models.Model):
    owner = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_in_group")
    group = models.ForeignKey(ChatGroupsName, on_delete=models.CASCADE, related_name="group_user")


class ChatInGroups(models.Model):
    text = models.CharField(max_length=1024, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users_in_group")
    group = models.ForeignKey(ChatGroupsName, on_delete=models.CASCADE, related_name="group_users")
    image = models.ImageField(null=True, blank=True, verbose_name="Фото чата")
