# Generated by Django 4.0.4 on 2022-05-05 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson_app', '0011_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.IntegerField(),
        ),
    ]
