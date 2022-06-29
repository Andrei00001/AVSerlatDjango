from rest_framework import serializers

from comments_app.api.serializers.comments import CommentsSerializer
from like_app.models import Like, LikeComments


class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"
        read_only_fields = "user",

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source="user",
    )


class LikesCommentsSerializer(serializers.ModelSerializer):
    count_likes_comment = serializers.SerializerMethodField()

    def get_count_likes_comment(self, instance):
        return instance.like_comment_user.count()

    class Meta:
        model = LikeComments
        fields = "__all__"

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source="user",
    )
