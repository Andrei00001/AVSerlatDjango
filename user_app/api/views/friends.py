from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, \
    UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from user_app.api.serializers.friends import FriendsSerializer, UpdateFriendsSerializer

from user_app.models import Friends


class FriendsView(GenericViewSet, ListModelMixin, CreateModelMixin, DestroyModelMixin):
    serializer_class = FriendsSerializer
    queryset = Friends.objects.all()


class UpdateFriendsView(GenericViewSet, RetrieveModelMixin, UpdateModelMixin):
    serializer_class = UpdateFriendsSerializer
    queryset = Friends.objects.all()
