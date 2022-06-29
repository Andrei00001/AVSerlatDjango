from rest_framework import serializers

from comments_app.api.serializers.comments import CommentsSerializer
from like_app.models import Like, LikeComments
from profile_app.api.serializers.profile import UserSerializer


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
    class Meta:
        model = LikeComments
        fields = "__all__"
        read_only_fields = "user",

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source="user",
    )
