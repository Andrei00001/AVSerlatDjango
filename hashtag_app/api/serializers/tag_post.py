from rest_framework import serializers

from posts_app.models import Post
from profile_app.api.serializers.profile import UserSerializer


class TagsPostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = "created_at", "title", "text", "is_public", "user"
