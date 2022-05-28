from rest_framework import routers


from like_app.api.views.like_view import LikesViewSet, LikesCommentsViewSet

api_router = routers.DefaultRouter()
api_router.register("like", LikesViewSet)
api_router.register("like_comments", LikesCommentsViewSet)
