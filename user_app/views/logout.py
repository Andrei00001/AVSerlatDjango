from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views import View


class Logout_user(View):
    def get(self, request):
        logout(request)
        return redirect("login")