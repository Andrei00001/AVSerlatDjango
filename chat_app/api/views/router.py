from rest_framework import routers

from chat_app.api.views.chat import ChatView


api_router = routers.DefaultRouter()
api_router.register("chat", ChatView)
