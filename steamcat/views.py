from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

def index(request):
    context = {
        "title":"steamofficial.com",
    }
    return render(request, "steamcat/index.html", context=context)

def about(request):
    context={
        "title":"steamofficialaboutpage.com",
    }
    return render(request, "steamcat/about.html", context=context)

def notfound(request, exception):
    return HttpResponseNotFound("No hello steam(")