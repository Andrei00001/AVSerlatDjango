from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=64, null=False, blank=False, unique=True)
    url = models.CharField(max_length=128, null=False, blank=False)

    def __str__(self):
        return self.title

