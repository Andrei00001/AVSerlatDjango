from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from posts_app.views.add_post import AddPost
from posts_app.views.delete_post import DeletePpost
from posts_app.views.update_posts import UpdatePost

urlpatterns = [
    path('add_post/', AddPost.as_view(), name='add_post'),
    path('profile/update_post/<int:pk>/', UpdatePost.as_view(), name='update_post'),
    path('profile/delete/<int:pk>/', DeletePpost.as_view(), name='delete_post'),

]

