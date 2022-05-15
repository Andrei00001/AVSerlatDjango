from django.db import migrations, models


def created_profile_for_existing_user(apps, schemas_editor):
    user_model = apps.get_model("lesson_app", "User")
    profile_model = apps.get_model("lesson_app", "Profile")

    users = user_model.objects.filter(profile__isnull=True).all()
    for user in users:
        profile = profile_model(user=user)
        profile.save()


class Migration(migrations.Migration):
    dependencies = (
        ("lesson_app", "0003_alter_profile_user"),
    )

    operations = (
        migrations.RunPython(created_profile_for_existing_user),
    )
