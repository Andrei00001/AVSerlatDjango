from django.db.models.signals import post_save

from django.dispatch import receiver


from profile_app.models import Profile
from user_app.models import User


@receiver(post_save, sender=User)
def post_save_user(**kwargs):
    instance = kwargs["instance"]

    user = User.objects.get(pk=instance.id)

    created = kwargs["created"]

    if created:
        user_add = Profile(user=user)
        user_add.save()
