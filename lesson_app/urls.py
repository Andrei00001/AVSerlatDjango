"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from lesson_app.views.delete_post import DeletePpost

from lesson_app.views.add_post import AddPost
from lesson_app.views.login import LoginUser
from lesson_app.views.logout import Logout_user
from lesson_app.views.main_page import Main_page
from lesson_app.views.delete_comment import DeleteCcomment
from lesson_app.views.profile import Profile_user
from lesson_app.views.profile_update import UserUpd
from lesson_app.views.register import RegisterUser
from lesson_app.views.update_ava import UpdateProfileAva
from lesson_app.views.update_posts import UpdatePost

urlpatterns = [
    path('', Main_page.as_view(), name='main_page'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', Logout_user.as_view(), name='logout'),
    path('profile/', Profile_user.as_view(), name='profile'),
    path('profile/update/', UserUpd.as_view(), name='profile_update'),
    path('profile/update/ava/<int:pk>/', UpdateProfileAva.as_view(), name='profile_update_ava'),
    path('add_post/', AddPost.as_view(), name='add_post'),
    path('profile/update_post/<int:pk>/', UpdatePost.as_view(), name='update_post'),
    path('profile/delete/<int:pk>/', DeletePpost.as_view(), name='delete_post'),
    path('profile/delete/comment/<int:pk>/', DeleteCcomment.as_view(), name='delete_comment'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
