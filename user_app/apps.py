from django.apps import AppConfig


class LessonAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_app'

    def ready(self):
        import user_app.signals.register_user
