from rest_framework import serializers

from comments_app.models import Comments
from hashtag_app.models import PostTags, Tags
from posts_app.models import Post, ImagePost
from user_app.models import User


class PostImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagePost
        fields = "image",


class PostUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "username", "last_name", "first_name", "email"


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = "tag",


class PostTagsSerializer(serializers.ModelSerializer):
    tag = TagsSerializer(read_only=True)

    class Meta:
        model = PostTags
        fields = "tag",


class PostSerializer(serializers.HyperlinkedModelSerializer):
    post_img = PostImgSerializer(many=True, read_only=True)
    user = PostUserSerializer(read_only=True)
    tag_post = PostTagsSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = (
            "title",
            "text",
            "created_at",
            "user",
            "post_img",
            "tag_post",

        )

    # publisher_user = serializers.HiddenField(
    #     default=serializers.CurrentUserDefault(),
    #     source="user",
    # )
