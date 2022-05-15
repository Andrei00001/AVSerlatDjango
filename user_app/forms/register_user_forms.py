from django import forms
from django.contrib.auth.forms import UserCreationForm

from user_app.models import User


class RegisterUserForms(UserCreationForm):
    username = forms.CharField(label="Логин")
    last_name = forms.CharField(label="Имя")
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Повтор пароля", widget=forms.PasswordInput())

    class Meta:
        model = User

        fields = ("username", "last_name", "password1", "password2", "email")
