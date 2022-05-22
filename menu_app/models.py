from django.db import models


class ClassMenu(models.Model):
    title = models.CharField(max_length=64, null=False, blank=False, unique=True)

    def __str__(self):
        return self.title


class Menu(models.Model):
    title = models.CharField(max_length=64, null=False, blank=False)
    url = models.CharField(max_length=128, null=False, blank=False)
    type = models.ForeignKey(ClassMenu, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
