from rest_framework import filters
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from posts_app.api.serializers.post import PostSerializer
from posts_app.models import Post


class PostView(GenericViewSet, ListModelMixin, CreateModelMixin):
    serializer_class = PostSerializer
    queryset = Post.objects.filter()
    filter_backends = [filters.OrderingFilter]
