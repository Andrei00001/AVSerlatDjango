# Generated by Django 4.0.4 on 2022-05-26 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments_app', '0005_comments_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='like',
        ),
    ]