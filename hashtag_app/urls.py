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

from hashtag_app.api.views.hashtag import TagsView
from hashtag_app.api.views.router import api_router
from hashtag_app.api.views.tag_post import TagsPostView
from hashtag_app.views.cloud import PostTagCloud
from hashtag_app.views.tags import PostTag


urlpatterns = [
    path('tag_cloud/', login_required(PostTagCloud.as_view()), name='tag_cloud'),
    path('tag_post/<str:tag>/', login_required(PostTag.as_view()), name='post_tags'),
    path('api/tag_post/<str:tag>/', TagsPostView.as_view(), name='tags_post'),
    path('api/', include(api_router.urls)),


]


