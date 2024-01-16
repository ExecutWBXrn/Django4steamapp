from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound

from .models import Games, Category
db_data = Games.objects.all()
cat_db = Category.objects.all()
def index(request):
    context = {
        "title":"steamofficial.com",
        "DB_data":db_data,
    }
    return render(request, "steamcat/index.html", context=context)

def about(request):
    context={
        "title":"steamofficialaboutpage.com",
    }
    return render(request, "steamcat/about.html", context=context)

def cart(request):
    return HttpResponse("Your cart empty!")

def furtherinfo(request):
    context={
        "title":"developercorner",
    }
    return render(request, "steamcat/furtherinfo.html", context=context)
def log(request):
    return HttpResponse("This function not availabel yet")
def categories(request):
    context = {
        "title":"categories"
    }
    return render(request, "steamcat/categories.html", context=context)

def categories_id(request, cat_id):
    w=get_object_or_404(Category, slug=cat_id)
    context = {
        "title":w.name,
        "cat_id":cat_id,
        "db_data":db_data,
    }
    return render(request, "steamcat/category_id.html", context=context)

def aboutgame(request, game_slug):
    w=get_object_or_404(Games, slug=game_slug)
    context = {
        "title":w.game,
        "db":db_data,
        "game_slug":game_slug,
    }
    return render(request, "steamcat/gamefurinfo.html", context=context)

def notfound(request, exception):
    return HttpResponseNotFound("No hello steam(")