# Generated by Django 4.0.4 on 2022-05-16 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hashtag_app', '0001_initial'),
        ('posts_app', '0002_delete_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hashtag_app.tags'),
        ),
    ]
