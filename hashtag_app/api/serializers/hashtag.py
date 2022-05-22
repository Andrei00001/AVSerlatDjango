from rest_framework import serializers

from hashtag_app.models import Tags, PostTags


class TagsImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostTags
        fields = 'id', "tag"
