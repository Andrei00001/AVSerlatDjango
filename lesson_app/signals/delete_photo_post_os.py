import os

from django.db.models.signals import pre_save
from django.dispatch import receiver

from lesson_app.models import Post


@receiver(pre_save, sender=Post)
def post_save_user(sender, instance, **kwargs):
    if not instance.pk:
        return False
    if sender.objects.get(pk=instance.pk).image:
        old_img = sender.objects.get(pk=instance.pk).image
        new_img = instance.image
        if old_img != new_img:
            if os.path.isfile(old_img.path):
                os.remove(old_img.path)
        else:
            return False
