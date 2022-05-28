from rest_framework import routers

from posts_app.api.views.post import PostsView

api_router = routers.DefaultRouter()
api_router.register("posts", PostsView)
