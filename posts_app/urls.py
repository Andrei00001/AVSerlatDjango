from django.contrib.auth.decorators import login_required
from django.urls import path, include

from posts_app.api.views.router import api_router
from posts_app.views.add_post import AddPost
from posts_app.views.delete_post import DeletePost
from posts_app.views.update_posts import UpdatePost

urlpatterns = [
    path('add_post/', login_required(AddPost.as_view()), name='add_post'),
    path('profile/update_post/<int:pk>/', login_required(UpdatePost.as_view()), name='update_post'),
    path('profile/delete/<int:pk>/', login_required(DeletePost.as_view()), name='delete_post'),
    path('api/', include(api_router.urls)),

]

