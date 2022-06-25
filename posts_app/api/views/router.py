from rest_framework import routers

from posts_app.api.views.post import PostsView, PostsImageView

api_router = routers.DefaultRouter()
api_router.register("posts", PostsView)
api_router.register("image_in_post", PostsImageView)
