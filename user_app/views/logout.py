from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views import View


class Logout_user(View):
    def post(self, request):
        logout(request)
        return redirect("login")