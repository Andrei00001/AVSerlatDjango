# Generated by Django 4.0.4 on 2022-05-22 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts_app', '0009_alter_post_user'),
        ('hashtag_app', '0007_alter_posttags_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posttags',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts_app.post'),
        ),
        migrations.AlterField(
            model_name='posttags',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tag_post', to='hashtag_app.tags'),
        ),
    ]
