from rest_framework import filters
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet


from user_app.api.serializers.subscriptions import SubscriptionsSerializer
from user_app.models import Subscriptions


class SubscriptionsView(GenericViewSet, ListModelMixin, RetrieveModelMixin, CreateModelMixin, DestroyModelMixin):
    serializer_class = SubscriptionsSerializer
    queryset = Subscriptions.objects.all()

