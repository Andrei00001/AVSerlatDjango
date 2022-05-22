import os
import re
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from hashtag_app.models import Tags, PostTags
from posts_app.models import Post


@receiver(post_save, sender=Post)
def post_save_user(sender, instance, **kwargs):
    if not instance.pk:
        return False
    post = Post.objects.get(pk=instance.id)

    tags = re.findall(r"#\w+", instance.text)
    if tags:
        for tag in tags:
            z = Tags.objects.filter(tag=tag)
            print(z)
            if not z:
                tag_obj = Tags(tag=tag.lower())
                tag_obj.save()
                PostTags.objects.create(tag=tag_obj, post=post)
            else:
                z = Tags.objects.get(tag=tag.lower())
                PostTags.objects.create(tag=z, post=post)

    print(tags, "signals")
