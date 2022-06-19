from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, \
    UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from chat_app.api.serializers.chat import ChatSerializer
from chat_app.models import Chat


class ChatView(GenericViewSet, ListModelMixin, CreateModelMixin, DestroyModelMixin):
    serializer_class = ChatSerializer
    queryset = Chat.objects.all()



