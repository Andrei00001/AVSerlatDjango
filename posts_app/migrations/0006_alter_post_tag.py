# Generated by Django 4.0.4 on 2022-05-17 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts_app', '0005_remove_post_tag_post_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
