from django.apps import AppConfig


class PostsAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'posts_app'

    def ready(self):
        import posts_app.signals.photo_delete_post_os
        import posts_app.signals.delete_photo_post_update_os
        import posts_app.signals.add_tag_table_tag