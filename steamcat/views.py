from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

db_data = [
    {"id":1, "game":"Cyberpunk 2077", "year":2020,"describe":"Cyberpunk 2077 is an open-world, action-adventure RPG set in the dark future of Night City — a dangerous megalopolis obsessed with power, glamor, and ceaseless body modification.", "price":"1000UAN","url":"https://store.steampowered.com/app/1091500/Cyberpunk_2077/" ,"is_published":True},
    {"id":2, "game":"S.T.A.L.K.E.R. 2: Heart of Chornobyl", "year":"Q1 2024","describe":"Discover the vast Chornobyl Exclusion Zone full of dangerous enemies, deadly anomalies and powerful artifacts. Unveil your own epic story as you make your way to the Heart of Chornobyl. Make your choices wisely, as they will determine your fate in the end.", "price":"895UAN","url":"https://store.steampowered.com/app/1643320/STALKER_2_Heart_of_Chornobyl/", "is_published":True},
    {"id":3, "game":"ELDEN RING", "year":2022 ,"describe":"THE NEW FANTASY ACTION RPG. Rise, Tarnished, and be guided by grace to brandish the power of the Elden Ring and become an Elden Lord in the Lands Between.", "price":"1799UAN","url":"https://store.steampowered.com/app/1245620/ELDEN_RING/" ,"is_published":True},
]

cat_db = [
    {"id":1, "title":"Sci-Fi"},
    {"id":2, "title":"Sport"},
    {"id":3, "title":"RPG"},
    {"id":4, "title":"Shooter"},
]
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

def notfound(request, exception):
    return HttpResponseNotFound("No hello steam(")