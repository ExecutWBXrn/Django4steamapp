from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

def index(request):
    return HttpResponse("Hello steam")

def notfound(request, exception):
    return HttpResponseNotFound("No hello steam(")