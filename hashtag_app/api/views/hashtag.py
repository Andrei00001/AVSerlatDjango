from rest_framework import filters
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from hashtag_app.api.serializers.hashtag import TagsImgSerializer
from hashtag_app.models import Tags


class TagsView(GenericViewSet, ListModelMixin, CreateModelMixin):
    serializer_class = TagsImgSerializer
    queryset = Tags.objects.filter()
    filter_backends = [filters.OrderingFilter]
