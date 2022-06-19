from django.contrib import messages
from django.contrib.auth import login
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import redirect, render
from django.views.generic import CreateView

from Project.settings import EMAIL_HOST_USER
from user_app.forms.register_user_forms import RegisterUserForms
from user_app.tasks import send_email_for_verify


class RegisterUser(CreateView):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('posts')
        form = RegisterUserForms
        context = {
            'title': 'Регистрация ',
            'form': form
        }
        return render(request, 'user_app/register.html', context)

    def post(self, request):
        form = RegisterUserForms(request.POST)
        if form.is_valid():
            user = form.save()

            # Отправка письма для верификации почты (написано в utils.py)

            current_site = get_current_site(request)
            # Получаем домен перед передачей в celery так как celery может принимать только конкретные значения

            send_email_for_verify.delay(current_site.domain, user.id)

            # EmailMessage(
            #     subject="asdf",
            #     body="adsfadsf",
            #     from_email=EMAIL_HOST_USER,
            #     to=[user.email]
            # ).send(fail_silently=False)
            return redirect('confirm_email')

        else:
            messages.error(request, 'Ошибка регистрации. Попробуйте снова')
            context = {
                'title': 'Регистрация ',
                'form': form
            }
            return render(request, 'user_app/register.html', context)
