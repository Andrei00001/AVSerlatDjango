from django.contrib.auth.decorators import login_required
from django.urls import path

from profile_app.api.views.profile import UserView
from profile_app.views.profile import *
from profile_app.views.profile_update import UserUpd
from profile_app.views.update_ava import UpdateProfileAva


urlpatterns = [
    path('profile/', login_required(Profile_user.as_view()), name='profile'),
    path('profile/<str:peopl>', login_required(ProfilePeoples_user.as_view()), name='profile_peoples'),
    path('profile/update/', login_required(UserUpd.as_view()), name='profile_update'),
    path('profile/update/ava/<int:pk>/', login_required(UpdateProfileAva.as_view()), name='profile_update_ava'),
    path('profile/add_friend/<str:peopl>/', login_required(AddFriend.as_view()), name='add_friend'),
    path('profile/confirmation_friend/<str:peopl>/', login_required(ConfirmationFriend.as_view()), name='confirmation_friend'),
    path('profile/del_friend/<str:peopl>/', login_required(DelFriend.as_view()), name='del_friend'),
    path('profile/add_subscription/<str:peopl>/', login_required(AddSubscription.as_view()), name='add_subscription'),
    path('profile/del_subscription/<str:peopl>/', login_required(DelSubscription.as_view()), name='del_subscription'),
    path('api/user', UserView.as_view({"get": "list", "post": "create"}), name='api_main_page'),
]

