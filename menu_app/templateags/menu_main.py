from django import template

from menu_app.models import Menu

register = template.Library()


@register.inclusion_tag('base.html')
def main_menu():
    menu = Menu.objects.all()
    return {'menu': menu}
