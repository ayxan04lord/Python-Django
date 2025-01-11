from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import render

def index(request):
    context = {
        "title" : "Home", 
        
    }

    return render(request, "news/index.html", context)

def about(request):
    return render(request, "news/about.html", {"title" : "About"})

def contact(request):
    return render(request, "news/contact-us.html", {"title" : "Contact" })

# def index(request):
#     return HttpResponse("<h1>Home Page</h1>")



# def contact(request):
#     return HttpResponse("<h1>Contact page</h1>")

# def category(request, catID):
#     return HttpResponse(f"Category {catID}")

# def archive(request, year):
#     if int(year) > 2024:
#         raise Http404()
#     return HttpResponse(f"Arxivde {year} uzre axtaris")

def pageNotFound(request, exception):
    return HttpResponseNotFound("UPSSS! Sehife tapilmadi")