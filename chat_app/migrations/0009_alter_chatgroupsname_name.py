# Generated by Django 4.0.4 on 2022-06-25 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_app', '0008_chatgroupsname_chatgroups'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatgroupsname',
            name='name',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Имя группы'),
        ),
    ]
