from django import template

from config import settings

register = template.Library()


@register.filter
def mediapath(value):
    return f'/media/{value}'
