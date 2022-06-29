from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from ..serializers.like import LikesSerializer, LikesCommentsSerializer
from ...models import Like, LikeComments


class LikesViewSet(GenericViewSet, ListModelMixin, CreateModelMixin):
    serializer_class = LikesSerializer
    queryset = Like.objects.all()


class LikesCommentsViewSet(GenericViewSet, ListModelMixin,RetrieveModelMixin, CreateModelMixin):
    serializer_class = LikesCommentsSerializer
    queryset = LikeComments.objects.all()
    lookup_field = 'comment_id'
