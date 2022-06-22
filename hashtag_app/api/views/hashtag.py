from rest_framework import filters
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from hashtag_app.api.serializers.hashtag import TagsImgSerializer, TagsCountSerializer
from hashtag_app.models import Tags, PostTags


class TagsView(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    serializer_class = TagsImgSerializer
    queryset = Tags.objects.all()
    action_serializer = {"retrieve": TagsCountSerializer}
    lookup_field = 'tag'

    def get_serializer_class(self):
        return self.action_serializer.get(self.action, self.serializer_class)
