from rest_framework import serializers

from user_app.models import Friends


class FriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friends
        fields = "__all__"
        read_only_fields = "user", "confirmation"

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source="user",
    )


class UpdateFriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friends
        fields = "__all__"
        read_only_fields = "user", "friend"

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source="user",
    )
