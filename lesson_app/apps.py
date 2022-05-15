from django.apps import AppConfig


class LessonAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lesson_app'

    def ready(self):
        import lesson_app.signals.register_user
        import lesson_app.signals.delete_photo_post_update_os
        import lesson_app.signals.delete_photo_user_update_os
        import lesson_app.signals.photo_delete_post_os
