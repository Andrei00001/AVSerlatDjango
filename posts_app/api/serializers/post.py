from rest_framework import serializers

from comments_app.api.serializers.comments import CommentsSerializer
from hashtag_app.models import PostTags, Tags
from like_app.models import Like
from posts_app.models import Post, ImagePost
from profile_app.api.serializers.profile import UserSerializer


class PostImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagePost
        fields = "image", "post_image"


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = "tag",


class PostTagsSerializer(serializers.ModelSerializer):
    tag = TagsSerializer(read_only=True)

    class Meta:
        model = PostTags
        fields = "tag",


class LikePostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Like
        fields = "user", "like_user"

    like_user = serializers.SerializerMethodField()

    def get_like_user(self, instance):
        return instance.user.count()


class PostSerializer(serializers.ModelSerializer):
    post_img = PostImgSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)
    tag_post = PostTagsSerializer(many=True, read_only=True)
    post_comments = CommentsSerializer(many=True, read_only=True)
    like_user = LikePostSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = "__all__"

        extra_kwargs = {
            "file": {
                "required": True,
                "write_only": True,
                "help_text": "Медиа"
            }

        }

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source="user",
    )
