# Generated by Django 4.0.4 on 2022-05-16 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hashtag_app', '0001_initial'),
        ('posts_app', '0003_post_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tag',
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(blank=True, null=True, to='hashtag_app.tags'),
        ),
    ]