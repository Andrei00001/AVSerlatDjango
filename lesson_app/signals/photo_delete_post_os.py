import os

from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver

from lesson_app.models import Post, ImagePost


@receiver(pre_delete, sender=Post)
def post_save_user(sender, instance, **kwargs):
    if not instance.pk:
        return False
    get_image = ImagePost.objects.filter(post_image=instance.pk)
    for post_image in get_image:
        if post_image.image:
            os.remove(post_image.image.path)
