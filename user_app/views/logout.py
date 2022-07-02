from django.contrib.auth import logout
from django.shortcuts import redirect, render
from django.views import View


class Logout_user(View):
    def get(self, request):
        return render(request, "user_app/login.html")

    def post(self, request):
        logout(request)
        return self.get(request)
