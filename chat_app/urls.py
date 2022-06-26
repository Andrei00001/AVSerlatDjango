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
from django.contrib.auth.decorators import login_required
from django.urls import path, include

from chat_app.api.views.router import api_router
from chat_app.views.add_chat_in_group_or_add_user_in_group import AddChatInGroupOrAddUser, AddUserInGroupOrAddUser
from chat_app.views.add_folder import AddFolder, AddFolderGroups
from chat_app.views.add_group_chat import AddGroup

from chat_app.views.chat_massege import Chat_page
from chat_app.views.seargh_group import UserSearchListView
from chat_app.views.you_chats import Chats

urlpatterns = [
    path('search/', UserSearchListView.as_view(), name='search_group'),
    path('friends/chat/<str:username>', login_required(Chat_page.as_view()), name='friends_chat'),
    path('chats/', login_required(Chats.as_view()), name='you_chats'),
    path('chats/add_groups', login_required(AddGroup.as_view()), name='add_groups'),
    path('chats/add_folder/', login_required(AddFolder.as_view()), name='add_folder'),
    path('chats/<int:chat>', login_required(AddChatInGroupOrAddUser.as_view()), name='groups_chat'),
    path('chats/group/<int:group>', login_required(AddFolderGroups.as_view()), name='groups_folder'),
    path('add_user_chats/<int:chat>', login_required(AddUserInGroupOrAddUser.as_view()), name='add_user_group'),
    path('api/', include(api_router.urls)),
]
