# Generated by Django 4.0.4 on 2022-05-26 20:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comments_app', '0002_rename_text_comments_text_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='like',
            field=models.ManyToManyField(related_name='like_comment', to=settings.AUTH_USER_MODEL),
        ),
    ]
