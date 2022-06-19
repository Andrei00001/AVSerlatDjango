from rest_framework import serializers

from profile_app.api.serializers.profile import UserSerializer
from user_app.models import Subscriptions


class SubscriptionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscriptions
        fields = "__all__"
        read_only_fields = "user",

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source="user",
    )
