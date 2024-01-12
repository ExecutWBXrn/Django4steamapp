from django import template
import steamcat.views as views
from steamcat.models import Games

register = template.Library()

@register.simple_tag(name='cat')
def categories():
    return views.cat_db

@register.simple_tag()
def menu():
    mainmenu = [
        {"mainword": "home", "url": "home"},
        {"mainword": "about site", "url": "about"},
        {"mainword": "cart", "url": "cart"},
        {"mainword": "further information about us", "url": "fname"},
        {"mainword": "log in", "url": "log"},
        {"mainword": "categories", "url": "cat"}
    ]
    return mainmenu