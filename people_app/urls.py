from django.contrib.auth.decorators import login_required
from django.urls import path

from people_app.view.people_view import PeopleView


urlpatterns = [
    path('people/', login_required(PeopleView.as_view()), name='people'),

]

