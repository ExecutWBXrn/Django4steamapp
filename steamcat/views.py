from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

def index(request):
    return render(request, "steamcat/index.html")

def about(request):
    return render(request, "steamcat/about.html")

def notfound(request, exception):
    return HttpResponseNotFound("No hello steam(")