from django.urls import path, register_converter
from .views import *
from .converter import *
register_converter(PriceConverter, "price")

urlpatterns = [
    path('', index, name="home"),
    path("about/", about, name="about"),
    path("cart/", cart, name="cart"),
    path("furtherinfo/", furtherinfo, name="fname"),
    path("log/", log, name="log"),
    path("categories/", categories, name="cat"),
    path("steam/<slug:game_slug>/", aboutgame, name="finfoaboutgame"),
]