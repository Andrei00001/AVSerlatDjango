from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from profile_app.views.profile import Profile_user
from profile_app.views.profile_update import UserUpd
from profile_app.views.update_ava import UpdateProfileAva
from main_page_app.views.main_page import Main_page

urlpatterns = [
    path('', Main_page.as_view(), name='main_page'),
    path('profile/', Profile_user.as_view(), name='profile'),
    path('profile/update/', UserUpd.as_view(), name='profile_update'),
    path('profile/update/ava/<int:pk>/', UpdateProfileAva.as_view(), name='profile_update_ava'),
]

