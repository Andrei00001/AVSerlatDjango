from rest_framework import serializers

from hashtag_app.api.serializers.hashtag import TagsImgSerializer
from hashtag_app.models import PostTags, Tags


class TagsPostCountSerializer(serializers.ModelSerializer):
    tag = TagsImgSerializer()

    class Meta:
        model = PostTags
        exclude = 'post'
