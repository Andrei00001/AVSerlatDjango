# Generated by Django 4.0.4 on 2022-06-25 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat_app', '0017_alter_foldergroups_folder'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chatgroupsname',
            old_name='name',
            new_name='title',
        ),
    ]
