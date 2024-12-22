from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    return HttpResponse("<h1>Home Page</h1>")

def about(request):
    return HttpResponse("<h1>About page</h1>")

def contact(request):
    return HttpResponse("<h1>Contact page</h1>")

def category(request, catID):
    return HttpResponse(f"Category {catID}")

def archive(request, year):
    return HttpResponse(f"Arxivde {year} uzre axtaris")