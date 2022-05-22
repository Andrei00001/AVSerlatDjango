# Generated by Django 4.0.4 on 2022-05-22 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hashtag_app', '0002_posttags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posttags',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tag_post', to='hashtag_app.tags'),
        ),
    ]
