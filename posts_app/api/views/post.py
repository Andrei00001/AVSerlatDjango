from rest_framework import filters
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from posts_app.api.serializers.post import PostSerializer
from posts_app.models import Post


class PostsView(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

