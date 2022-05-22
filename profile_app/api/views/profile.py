from rest_framework import filters
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from profile_app.api.serializers.profile import *
from user_app.models import User


class UserView(GenericViewSet, ListModelMixin, CreateModelMixin):
    serializer_class = UserSerializer
    queryset = User.objects.filter()
    filter_backends = [filters.OrderingFilter]



