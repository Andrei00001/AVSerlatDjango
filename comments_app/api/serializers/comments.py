from rest_framework import serializers

from comments_app.models import Comments
from like_app.models import LikeComments
from profile_app.api.serializers.profile import UserSerializer


class LikeCommentsSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = LikeComments
        fields = "user",


class CommentsSerializer(serializers.ModelSerializer):
    like_comment_user = LikeCommentsSerializer(many=True, read_only=True)

    class Meta:
        model = Comments
        fields = "__all__"
        read_only_fields = "user",

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source="user",
    )
