from rest_framework import routers

from hashtag_app.api.views.hashtag import TagsView
from hashtag_app.api.views.tag_post import TagsPostView

api_router = routers.DefaultRouter()

api_router.register("tag", TagsView)

