from rest_framework import serializers


from profile_app.models import Profile
from user_app.models import User


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "image",


class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "profile",
        )

    # publisher_user = serializers.HiddenField(
    #     default=serializers.CurrentUserDefault(),
    #     source="user",
    # )
