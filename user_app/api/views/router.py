from rest_framework import routers

from user_app.api.views.friends import FriendsView, UpdateFriendsView
from user_app.api.views.subscriptions import SubscriptionsView

api_router = routers.DefaultRouter()
api_router.register("subscriptions", SubscriptionsView)
api_router.register("friends", FriendsView)
api_router.register("friend", UpdateFriendsView)
