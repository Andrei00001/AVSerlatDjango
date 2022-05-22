from django.urls import path

from posts_app.api.views.post import PostView
from posts_app.views.add_post import AddPost
from posts_app.views.delete_post import DeletePpost
from posts_app.views.update_posts import UpdatePost

urlpatterns = [
    path('add_post/', AddPost.as_view(), name='add_post'),
    path('profile/update_post/<int:pk>/', UpdatePost.as_view(), name='update_post'),
    path('profile/delete/<int:pk>/', DeletePpost.as_view(), name='delete_post'),
    path('api/post', PostView.as_view({"get": "list", "post": "create"}), name='post_page'),

]

