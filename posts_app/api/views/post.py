from rest_framework import filters
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from posts_app.api.serializers.post import PostSerializer, PostImgSerializer
from posts_app.models import Post, ImagePost


class PostsView(GenericViewSet, ListModelMixin, RetrieveModelMixin, CreateModelMixin):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostsImageView(GenericViewSet, ListModelMixin, CreateModelMixin):
    serializer_class = PostImgSerializer
    queryset = ImagePost.objects.all()
