from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

db_data = [
    {"id":1, "game":"Cyberpunk 2077", "year":2020,"describe":"Cyberpunk 2077 is an open-world, action-adventure RPG set in the dark future of Night City — a dangerous megalopolis obsessed with power, glamor, and ceaseless body modification.", "price":"1000UAN", "is_published":True},
    {"id":2, "game":"S.T.A.L.K.E.R. 2: Heart of Chornobyl", "year":"Q1 2024","describe":"Discover the vast Chornobyl Exclusion Zone full of dangerous enemies, deadly anomalies and powerful artifacts. Unveil your own epic story as you make your way to the Heart of Chornobyl. Make your choices wisely, as they will determine your fate in the end.", "price":"895UAN", "is_published":True},
    {"id":3, "game":"ELDEN RING", "year":2022 ,"describe":"THE NEW FANTASY ACTION RPG. Rise, Tarnished, and be guided by grace to brandish the power of the Elden Ring and become an Elden Lord in the Lands Between.", "price":"1799UAN", "is_published":True},
]
def index(request):
    context = {
        "title":"steamofficial.com",
        "menu":["about site", "cart", "further information about us", "log in"],
        "DB_data":db_data,
    }
    return render(request, "steamcat/index.html", context=context)

def about(request):
    context={
        "title":"steamofficialaboutpage.com",
    }
    return render(request, "steamcat/about.html", context=context)

def notfound(request, exception):
    return HttpResponseNotFound("No hello steam(")