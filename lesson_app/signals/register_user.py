import os

from django.db.models.signals import post_save, m2m_changed, pre_save

from django.dispatch import receiver

from lesson_app.models import Profile, User


@receiver(post_save, sender=User)
def post_save_user(**kwargs):
    instance = kwargs["instance"]

    user = User.objects.get(pk=instance.id)

    created = kwargs["created"]

    if created:
        user_add = Profile(user=user)
        user_add.save()



# @receiver(pre_save, sender=Profile)
# def post_save_user(**kwargs):
#     instance = kwargs["instance"]
#     created = kwargs["created"]
#     if not created:
#         image = Profile.objects.get(pk=instance.id)
#         print(image.image)
#         # if image:
#         #     path = f".\media\{image.image}"
#         #     os.remove(path)
#