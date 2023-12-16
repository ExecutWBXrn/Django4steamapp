from django.urls import path, register_converter
from .views import *
from .converter import *
register_converter(PriceConverter, "price")

urlpatterns = [
    path('', index, name="home"),
    path("about/", about, name="about"),
]