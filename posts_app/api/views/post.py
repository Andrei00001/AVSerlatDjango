from rest_framework import filters
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from posts_app.api.serializers.post import PostSerializer, PostImgSerializer, LikePostSerializer
from posts_app.models import Post, ImagePost


class PostsView(GenericViewSet, ListModelMixin, RetrieveModelMixin, CreateModelMixin):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    action_serializer = {"retrieve": LikePostSerializer}
    lookup_field = 'posts'

    def get_serializer_class(self):
        return self.action_serializer.get(self.action, self.serializer_class)


class PostsImageView(GenericViewSet, ListModelMixin, CreateModelMixin):
    serializer_class = PostImgSerializer
    queryset = ImagePost.objects.all()
