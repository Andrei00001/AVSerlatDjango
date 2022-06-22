from rest_framework import serializers

from hashtag_app.api.views.tag_post import TagsPostView
from hashtag_app.models import Tags, PostTags
from posts_app.api.serializers.post import PostSerializer


class TagsImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'

    count_post = serializers.SerializerMethodField()

    def get_count_post(self, instance):
        return instance.post_tag.count()


class TagsPostSerializer(serializers.ModelSerializer):
    post = PostSerializer(read_only=True)

    class Meta:
        model = PostTags
        fields = 'post',


class TagsCountSerializer(serializers.ModelSerializer):
    post_tag = TagsPostSerializer(many=True, read_only=True)

    class Meta:
        model = Tags
        fields = 'id', 'tag', 'count_post', 'post_tag'

    count_post = serializers.SerializerMethodField()

    def get_count_post(self, instance):
        return instance.post_tag.count()
