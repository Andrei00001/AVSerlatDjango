from rest_framework import serializers

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
    class Meta:
        model = LikeComments
        fields = "__all__"
        read_only_fields = "user",

        count_likes = serializers.SerializerMethodField()

        def get_count_likes(self, instance):
            return instance.like_comment_user.count()

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source="user",
    )
