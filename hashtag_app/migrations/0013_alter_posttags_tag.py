# Generated by Django 4.0.4 on 2022-05-22 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hashtag_app', '0012_alter_posttags_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posttags',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tag_tag', to='hashtag_app.tags'),
        ),
    ]
