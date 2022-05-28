from rest_framework import routers

from comments_app.api.views.comments_view import CommentsViewSet

api_router = routers.DefaultRouter()
api_router.register("comments", CommentsViewSet)
