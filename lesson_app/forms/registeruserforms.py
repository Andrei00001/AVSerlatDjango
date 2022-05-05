from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterUserForms(UserCreationForm):
    username = forms.CharField(label="Логин")
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Пароль")
    password2 = forms.CharField(label="Повтор пароля")

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")
