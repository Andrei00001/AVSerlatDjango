from django import template

from menu_app.models import Menu

register = template.Library()


@register.inclusion_tag('base.html')
def main_menu():
    menu = Menu.objects.filter(type=1)
    return {'menu': menu, }


@register.inclusion_tag('base.html')
def profile_menu():
    menu = Menu.objects.filter(type=2)
    return {'menu': menu, }


@register.inclusion_tag('base.html', takes_context=True)
def user_menu(context):
    if context.request.user.is_authenticated:
        menu = [
            {
                'title': f"{context.request.user.last_name} {context.request.user.first_name}",
                'url': '/profile',
            },
            {
                'title': 'Выйти',
                'url': '/logout/',
            },
        ]
    else:
        menu = [
            {
                'title': 'Войти',
                'url': '/login',
            },
            {
                'title': 'Регистрация',
                'url': '/registration',
            },
        ]

    return {'menu': menu, }