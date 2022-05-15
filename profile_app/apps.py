from django.apps import AppConfig


class ProfileAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profile_app'

    def ready(self):
        import profile_app.signals.delete_photo_user_update_os

