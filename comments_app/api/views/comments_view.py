from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from comments_app.api.serializers.comments import CommentsSerializer
from ...models import Comments


class CommentsViewSet(GenericViewSet,ListModelMixin,RetrieveModelMixin,CreateModelMixin ):
    serializer_class = CommentsSerializer
    queryset = Comments.objects.all()
