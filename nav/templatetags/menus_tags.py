"""nav/templatetags/menus_tags.py"""
from django import template

from ..models import Menu

register = template.Library()


@register.simple_tag()
def get_menu(slug):
    return Menu.objects.get(slug=slug)


@register.filter(name='active')
def set_active(value, url):
    # print(value, url)
    # match = re.search(value, url)
    if(value == url):
        return 'active'
    else:
        return ''
