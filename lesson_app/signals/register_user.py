
from django.db.models.signals import post_save
from django.dispatch import receiver

from lesson_app.models import Profile, User


@receiver(post_save, sender=User)
def post_save_user(**kwargs):
    instance = kwargs["instance"]

    user = User.objects.get(pk=instance.id)

    created = kwargs["created"]

    if created:
        print("Создан")
        user_add = Profile(user=user, image="def.jpg")
        user_add.save()
