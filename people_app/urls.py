from django.urls import path, include

from people_app.view.people_view import PeopleView
from posts_app.api.views.router import api_router
from posts_app.views.add_post import AddPost
from posts_app.views.delete_post import DeletePpost
from posts_app.views.update_posts import UpdatePost

urlpatterns = [
    path('people/', PeopleView.as_view(), name='people'),

]

