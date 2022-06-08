from django.urls import path

from profile_app.api.views.profile import UserView
from profile_app.views.profile import *
from profile_app.views.profile_update import UserUpd
from profile_app.views.update_ava import UpdateProfileAva


urlpatterns = [
    path('profile/', Profile_user.as_view(), name='profile'),
    path('profile/<str:peopl>', ProfilePeoples_user.as_view(), name='profile_peoples'),
    path('profile/update/', UserUpd.as_view(), name='profile_update'),
    path('profile/update/ava/<int:pk>/', UpdateProfileAva.as_view(), name='profile_update_ava'),
    path('profile/add_friend/<str:peopl>/', AddFriend.as_view(), name='add_friend'),
    path('profile/confirmation_friend/<str:peopl>/', ConfirmationFriend.as_view(), name='confirmation_friend'),
    path('profile/del_friend/<str:peopl>/', DelFriend.as_view(), name='del_friend'),
    path('profile/add_subscription/<str:peopl>/', AddSubscription.as_view(), name='add_subscription'),
    path('profile/del_subscription/<str:peopl>/', DelSubscription.as_view(), name='del_subscription'),
    path('api/user', UserView.as_view({"get": "list", "post": "create"}), name='api_main_page'),
]

