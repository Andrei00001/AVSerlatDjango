from django.urls import path

from profile_app.api.views.profile import UserView
from profile_app.views.profile import Profile_user
from profile_app.views.profile_update import UserUpd
from profile_app.views.update_ava import UpdateProfileAva


urlpatterns = [
    path('profile/', Profile_user.as_view(), name='profile'),
    path('profile/update/', UserUpd.as_view(), name='profile_update'),
    path('profile/update/ava/<int:pk>/', UpdateProfileAva.as_view(), name='profile_update_ava'),
    path('api/user', UserView.as_view({"get": "list", "post": "create"}), name='api_main_page'),
]

