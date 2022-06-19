from rest_framework import serializers

from chat_app.models import Chat


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = "__all__"
        read_only_fields = "host_user", "created_at"

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source="host_user",
    )
